<svelte:options accessors={true} />

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block } from "@gradio/atoms";
	import type { LoadingStatus } from "@gradio/statustracker";
	import { tick } from "svelte";
	import { Color } from "dpmol/lib/mol-util";
	import {
		Format,
		Granularity,
		LightPlugin,
		RepresentationType,
		ThemeC,
	} from "dpmol/lib/light-plugin";
	import { VESTA_COLOR_TABLE } from "dpmol/lib/mol-theme/color/material-element-symbol";
	import { traverseAtoms } from "dpmol/lib/light-plugin/utils";
	import { Mat4, Vec3 } from "dpmol/lib/mol-math/linear-algebra";
	import { math } from "./math.js";
	import {
		sqrt,
		sin,
		cos,
		pi,
		dot,
		cross,
		norm,
		matrix,
		transpose,
		multiply,
		divide,
		abs,
		acos,
	} from "mathjs";

	export let gradio: Gradio<{
		change: never;
		submit: never;
		input: never;
		clear_status: LoadingStatus;
	}>;
	export let materialFile = "";
	export let value = "";
	export let value_is_output = false;
	export let height;

	window.process = {
		env: {
			NODE_ENV: "production",
			LANG: "",
		},
	};

	let lightPlugin = new LightPlugin();

	const guid = () => {
		function S4() {
			// eslint-disable-next-line no-bitwise
			return (((1 + Math.random()) * 0x10000) | 0)
				.toString(16)
				.substring(1);
		}
		return `${S4() + S4()}-${S4()}-${S4()}-${S4()}-${S4()}${S4()}${S4()}`;
	};
	const key = guid();
	$: key;

	let el: HTMLTextAreaElement | HTMLInputElement;
	const container = true;

	function handle_change(): void {
		gradio.dispatch("change");
		if (!value_is_output) {
			gradio.dispatch("input");
		}
	}

	async function handle_keypress(e: KeyboardEvent): Promise<void> {
		await tick();
		if (e.key === "Enter") {
			e.preventDefault();
			gradio.dispatch("submit");
		}
	}

	$: if (value === null) value = "";

	// When the value changes, dispatch the change event via handle_change()
	// See the docs for an explanation: https://svelte.dev/docs/svelte-components#script-3-$-marks-a-statement-as-reactive
	$: value, handle_change();

	let mousePosition = { x: -1000, y: -1000 };
	$: mousePosition;

	let tooltipText = "";
	$: tooltipText;
	function hexToColorString(hex) {
		let hexString = hex.toString(16);

		while (hexString.length < 6) {
			hexString = "0" + hexString;
		}

		return "#" + hexString;
	}
	let atomList = [];

	function ase2Material(ase) {
  const { length, angle, spacegroup: aseSpacegroup, atoms: aseAtoms } = ase[0]
  const material = {
    expand: Vec3.create(1, 1, 1),
    atoms: [],
    lattice: undefined
  }

  const lattice = (() => {
    if (!length || !angle || !aseSpacegroup) {
      return
    }
    const [a, b, c] = length
    const [alpha, beta, gamma] = angle
    const spacegroup = {
      symbol: aseSpacegroup[1],
      no: aseSpacegroup[0]
    }
    const lattice: any = createLatticeByParams({
      spacegroup,
      a,
      b,
      c,
      alpha,
      beta,
      gamma
    })
    lattice.parent = material
    return lattice
  })()

  const atoms = aseAtoms.map((item, index) => {
    const params = {
      element: item.formula,
      xyz: item.cart_coord,
      abc: item.frac_coord
    }
    const atom = createAtom(params, {
      lattice,
      order: index
    })
    atom.parent = material

    return atom
  })

  material.lattice = lattice
  material.atoms = atoms
  return material
}

	function combineElements(
		arr: number[],
		num = arr.length,
		combine = [] as number[][],
	): number[][] {
		if (num === 0) return [];
		if (num === 1) return [...combine, ...arr.map((n) => [n])];
		if (arr.length === num)
			return combineElements(arr, num - 1, [arr.slice()]);
		for (let i = 0; i < arr.length - 1; i++) {
			for (let j = i + 1; j < arr.length; j++) {
				combine.push([arr[i], arr[j]]);
			}
		}
		return combineElements(arr, num - 1, combine);
	}
	function getSymmetryAtoms(atoms, lattice) {
		const tolerance = 0.005;
		const symmetryAtoms = [];

		atoms.forEach((atom, idx) => {
			const { abc } = atom;
			if (!abc || abc[0] === undefined) return;

			{
				const zeroElements = [];
				if (Math.abs(abc[0]) <= tolerance) zeroElements.push(0);
				if (Math.abs(abc[1]) <= tolerance) zeroElements.push(1);
				if (Math.abs(abc[2]) <= tolerance) zeroElements.push(2);
				const coordPermutations = combineElements(zeroElements);
				const perms = coordPermutations.map((elements) => [
					Number(elements.includes(0)),
					Number(elements.includes(1)),
					Number(elements.includes(2)),
				]);
				perms.forEach((perm) => {
					const sAtom = createAtom(atom, {
						order: idx,
						lattice,
						symmetry: perm,
					});
					symmetryAtoms.push(sAtom);
				});
			}

			{
				const oneElements = [];
				if (Math.abs(1 - abc[0]) <= tolerance) oneElements.push(0);
				if (Math.abs(1 - abc[1]) <= tolerance) oneElements.push(1);
				if (Math.abs(1 - abc[2]) <= tolerance) oneElements.push(2);
				const coordPermutations = combineElements(oneElements);
				const perms = coordPermutations.map((elements) => [
					-Number(elements.includes(0)),
					-Number(elements.includes(1)),
					-Number(elements.includes(2)),
				]);
				perms.forEach((perm) => {
					const sAtom = createAtom(atom, {
						order: idx,
						lattice,
						symmetry: perm,
					});
					symmetryAtoms.push(sAtom);
				});
			}
		});

		return symmetryAtoms;
	}
	function createSymmetryMaterial(material) {
		if (!material.lattice) {
			return material;
		}
		const symmetryMaterial = createOriginalMaterial({
			lattice: material.lattice,
			atoms: material.atoms,
		});
		const { atoms } = symmetryMaterial;
		const symmetryAtoms = getSymmetryAtoms(atoms, material.lattice);

		symmetryMaterial.atoms = [...symmetryMaterial.atoms, ...symmetryAtoms];

		return symmetryMaterial;
	}
	function getParamsFromSymmetryMaterial(material: any) {
		const elements: string[] = [];
		const xyzs: number[][] = [];

		material.atoms.map((atom) => {
			elements.push(atom.element);
			xyzs.push(atom.xyz);
		});

		return {
			elements,
			xyzs,
			lattice: material.lattice,
		};
	}
	async function loadFile() {
		if (!lightPlugin.canvas3d) return;
		const [ref] = await lightPlugin.managers.representation.createMolecular(
			{
				format: Format.Material,
				reprType: RepresentationType.BallAndStick,
				data: getParamsFromSymmetryMaterial(
					createSymmetryMaterial(
						ase2Material(JSON.parse(materialFile)),
					),
				),
				theme: {
					[ThemeC.ATOM]: {
						color: {
							name: "material-element-symbol",
						},
					},
				},
			},
		);
		const atomSet = new Set();
		const structure = await lightPlugin.managers.cell.getStructure(ref);
		if (!structure) return;
		traverseAtoms(structure, (atom) => {
			atomSet.add(atom.typeSymbol);
		});
		atomList = new Array(...atomSet.values());

		// 创建晶胞
		lightPlugin.managers.representation.createOther({
			data: lightPlugin.managers.cell.getUnitCellData(ref),
			type: RepresentationType.UnitCell,
		});
		// 更新axes(不传ref即为恢复axes)
		lightPlugin.managers.camera.updateAxes(ref);
	}
	const aseToMaterial = (aseData: any) => {
		console.log(aseData[0])
		const { angle, atoms, length } = aseData[0];
		const [a, b, c] = length;
		const [alpha, beta, gamma] = angle;
		const res = {
			elements: [],
			xyzs: [],
			lattice: {
				a,
				b,
				c,
				alpha,
				beta,
				gamma,
			},
		};
		atoms.forEach((atom) => {
			const { cart_coord, formula } = atom;
			res.elements.push(formula);
			res.xyzs.push(cart_coord);
		});
		console.log(res);
		return res;
	};

	function createOriginalMaterial(params: { lattice?: any; atoms: any[] }) {
		const material = {
			expand: Vec3.create(1, 1, 1),
			atoms: [],
			lattice: undefined,
		};
		const lattice: any = params?.lattice
			? createLatticeByParams(params?.lattice)
			: undefined;
		if (lattice) {
			lattice.parent = material;
		}
		const atoms = params.atoms.map((a, index) => {
			const atom = createAtom(a, {
				lattice,
				order: index,
			});
			atom.parent = material;

			return atom;
		});

		material.lattice = lattice;
		material.atoms = atoms;
		return material;
	}

	function isSameVec(source: number[], target: number[]) {
		return source.every((n, i) => n === target[i]);
	}

	function isOriginVec(image: number[]) {
		return isSameVec(image, [0, 0, 0]);
	}

	function getTransMatrixFormSymmetryVec(symmetryVec: any, lattice: any) {
		const { vecA, vecB, vecC } = lattice;
		const transVec3 = Vec3.zero();
		if (symmetryVec[0])
			Vec3.scaleAndAdd(transVec3, transVec3, vecA, symmetryVec[0]);
		if (symmetryVec[1])
			Vec3.scaleAndAdd(transVec3, transVec3, vecB, symmetryVec[1]);
		if (symmetryVec[2])
			Vec3.scaleAndAdd(transVec3, transVec3, vecC, symmetryVec[2]);
		const transMatrix = Mat4.fromTranslation(Mat4.zero(), transVec3);
		return transMatrix;
	}

	function unitVector(x: number[]): number[] {
		const y = x.map((n) => n as number); // Ensure elements are numbers
		return divide(y, norm(y)) as number[];
	}
	function createAtom(
		params: any,
		extraParams?: {
			order?: number;
			lattice?: any;
			symmetry?: any;
		},
	): any {
		const { element } = params;
		const { order, lattice, symmetry } = extraParams || {};

		if (!params.abc && !params.xyz) {
			throw new Error("createAtom: Need xyz or abc!");
		}

		if (!lattice && !params.xyz) {
			throw new Error("createAtom: Need xyz or lattice!");
		}

		let abc = (() => {
			const { xyz, abc } = params;
			// case1: 非晶体，无abc，无lattice
			if (!lattice) {
				return undefined;
			}

			// case2: 晶体，非对称性，已有xyz，计算abc
			if (!abc) {
				return Vec3.create.apply(
					null,
					math.multiply(xyz!, lattice.invertMatrix),
				);
			}

			// case3: 晶体，非对称性，已有abc
			if (!symmetry || isOriginVec(symmetry)) {
				return Vec3.create(abc[0], abc[1], abc[2]);
			}

			// case4: 晶体，有对称性，已有abc，计算对称位置的abc
			const transMatrix = getTransMatrixFormSymmetryVec(
				symmetry,
				lattice,
			);
			const symmetryAbc = Vec3.transformMat4(
				Vec3.zero(),
				Vec3.create(abc[0], abc[1], abc[2]),
				transMatrix,
			);
			return symmetryAbc;
		})();

		let xyz = (() => {
			const { xyz, abc } = params;
			// case1: 非晶体，无lattice
			if (!lattice) {
				return Vec3.create(xyz![0], xyz![1], xyz![2]);
			}

			// case2: 晶体，非对称性，已有abc，计算xyz
			if (!xyz) {
				return Vec3.create.apply(
					null,
					math.multiply(abc!, lattice.matrix),
				);
			}

			// case3: 晶体，非对称性，已有xyz
			if (!symmetry || isOriginVec(symmetry)) {
				return Vec3.create(xyz[0], xyz[1], xyz[2]);
			}

			// case4: 晶体，有对称性，已有xyz，计算对称位置的xyz
			const transMatrix = getTransMatrixFormSymmetryVec(
				symmetry,
				lattice,
			);
			const symmetryXyz = Vec3.transformMat4(
				Vec3.zero(),
				Vec3.create(xyz[0], xyz[1], xyz[2]),
				transMatrix,
			);
			return symmetryXyz;
		})();

		// 超出晶格坐标，处理回晶格内
		// TODO: 浮点数计算精度问题需要解处理嘛？
		// const needRecalculate = abc && abc.some((n) => n < 0 || n > 1)
		// if (needRecalculate) {
		//   abc = Vec3.fromArray(
		//     Vec3.zero(),
		//     abc!.map((n) => n % 1).map((n) => (n > 0 ? n : 1 - n)),
		//     0
		//   )
		//   xyz = Vec3.transformMat4(
		//     Vec3.zero(),
		//     Vec3.create(abc![0], abc![1], abc![2]),
		//     lattice!.matrix
		//   )
		// }

		return {
			element,
			xyz,
			abc,
			order,
			symmetry,
		};
	}

	function cellparToCell(
		cellpar: number | number[],
		abNormal: number[] = [0, 0, 1],
		aDirection?: number[],
	): number[][] {
		if (!aDirection) {
			const crossProduct = cross(abNormal, [1, 0, 0]) as number[];
			if ((norm(crossProduct) as number) < 1e-5) {
				aDirection = [0, 0, 1];
			} else {
				aDirection = [1, 0, 0];
			}
		}

		const ad = aDirection;
		const Z = unitVector(abNormal);
		const X = unitVector(ad.map((v, i) => v - dot(ad, Z) * Z[i]));
		const Y = cross(Z, X) as number[];

		let alpha = 90,
			beta = 90,
			gamma = 90;
		let a, b, c;

		if (typeof cellpar === "number") {
			a = b = c = cellpar;
		} else if (cellpar.length === 1) {
			a = b = c = cellpar[0];
		} else if (cellpar.length === 3) {
			[a, b, c] = cellpar;
		} else {
			[a, b, c, alpha, beta, gamma] = cellpar;
		}

		const eps = 2 * Number.EPSILON; // around 1.4e-14

		let cosAlpha = abs(alpha - 90) < eps ? 0 : cos((alpha * pi) / 180);
		let cosBeta = abs(beta - 90) < eps ? 0 : cos((beta * pi) / 180);
		let cosGamma, sinGamma;

		if (abs(gamma - 90) < eps) {
			cosGamma = 0;
			sinGamma = 1;
		} else if (abs(gamma + 90) < eps) {
			cosGamma = 0;
			sinGamma = -1;
		} else {
			cosGamma = cos((gamma * pi) / 180);
			sinGamma = sin((gamma * pi) / 180);
		}

		const va = [a, 0, 0];
		const vb = [b * cosGamma, b * sinGamma, 0];
		const cx = cosBeta;
		const cy = (cosAlpha - cosBeta * cosGamma) / sinGamma;
		const czSqr = 1 - cx * cx - cy * cy;
		if (czSqr < 0)
			throw new Error("cz_sqr is negative, which is not possible");
		const cz = sqrt(czSqr) as number;

		const vc = [c * cx, c * cy, c * cz];

		const abc = matrix([va, vb, vc]);
		const T = matrix([X, Y, Z]);
		const cell = multiply(abc, transpose(T));

		return cell.toArray() as number[][];
	}
	function createLatticeByParams(params) {
		const { a, b, c, alpha, beta, gamma, spacegroup } = params;
		const matrix =
			params.matrix || cellparToCell([a, b, c, alpha, beta, gamma]);
		const invertMatrix = math.inv(matrix);

		const vecA = Vec3.create.apply(null, matrix[0]);
		const vecB = Vec3.create.apply(null, matrix[1]);
		const vecC = Vec3.create.apply(null, matrix[2]);

		const volume = Math.abs(Vec3.dot(vecA, vecA)) * c;

		return {
			spacegroup,
			a,
			b,
			c,
			volume,
			alpha,
			beta,
			gamma,
			vecA,
			vecB,
			vecC,
			matrix,
			invertMatrix,
		};
	}
	function init(): void {
		lightPlugin.managers.representation.showPolarHydrogenOnly = false;
		// 修改光照及hover select颜色
		lightPlugin.createCanvas(
			document.getElementById(`material-viewer-canvas-${key}`),
			{
				renderer: {
					ambientIntensity: 0.4,
					backgroundColor: Color(0xf2f5fa),
				},
			},
		);
		lightPlugin.managers.selection.structure.setGranularity(
			Granularity.Atom,
		);
		lightPlugin.managers.events.setAllowSelect(false);
		lightPlugin.managers.highlight.info.subscribe((data) => {
			if (data.info?.granularity === Granularity.Atom) {
				const { atomName, x, y, z } = data.info;
				tooltipText = `${atomName} (${[x, y, z].map((i) => i.toFixed(3)).join(", ")})`;
			} else {
				tooltipText = "";
			}
		});
		// @ts-ignore
		// eslint-disable-next-line no-underscore-dangle
		window.__material_viewer = lightPlugin;
		setTimeout(() => lightPlugin.refresh(), 50);
	}
	const interval = setInterval(() => {
		if (
			!!document.getElementById(`material-viewer-canvas-${key}`)
				?.clientHeight &&
			!lightPlugin.canvas3d
		) {
			clearInterval(interval);
			init();
			console.log(materialFile)
			loadFile();
		}
	}, 500);

	function updateFile() {
		if (!lightPlugin.canvas3d) return;
		lightPlugin.clear();
		loadFile();
	}
	$: materialFile, updateFile();

	const resize = () => {
		setTimeout(() => {
			lightPlugin.refresh({ fixCamera: true });
		}, 0);
	};
	$: height, resize();
</script>

<div class="material-viewer-container" style={`height: ${height}px;`}>
	<div
		id={`material-viewer-canvas-${key}`}
		style={"width: 100%;height: 100%;min-height: 240px;"}
		on:mousemove={(e) => {
			mousePosition = {
				x: e.offsetX,
				y: e.offsetY,
			};
		}}
	></div>
	{#if !!tooltipText}
		<div
			class="tooltip"
			style={`top: ${mousePosition.y - 45}px;left: ${mousePosition.x - 8}px;`}
		>
			<div class={"tooltip-inner"}>{tooltipText}</div>
		</div>
	{/if}
	<div class={"atom-model-legend-container"}>
		{#each atomList as atom}
			<div class={"atom-model-legend-item"}>
				<div
					style={`background-color: ${hexToColorString(VESTA_COLOR_TABLE[atom.toUpperCase()])}`}
					class={"atom-model-legend-item-ball"}
				/>
				{atom}
			</div>
		{/each}
	</div>
	<div class="material-viewer-toolbar">
		<button
			class="material-viewer-toolbar-btn"
			on:click={() => lightPlugin.managers.camera.zoomIn()}
		>
			<svg
				width="1em"
				height="1em"
				viewBox="0 0 16 16"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<path
					d="M8.02 3.334l-.012 9.333M3.336 8h9.333"
					stroke="#A2A5C4"
					stroke-width="1.3"
					stroke-linecap="round"
					stroke-linejoin="round"
				/>
			</svg>
		</button>
		<button
			class="material-viewer-toolbar-btn"
			on:click={() => lightPlugin.managers.camera.zoomOut()}
		>
			<svg
				width="1em"
				height="1em"
				viewBox="0 0 16 16"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<path
					d="M3.336 8h9.333"
					stroke="#A2A5C4"
					stroke-width="1.3"
					stroke-linecap="round"
					stroke-linejoin="round"
				/>
			</svg>
		</button>
		<button
			class="material-viewer-toolbar-btn"
			on:click={() => lightPlugin.managers.camera.reset()}
		>
			<svg
				width="1em"
				height="1em"
				viewBox="0 0 16 16"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<path
					d="M8.0026 14.6673C11.6845 14.6673 14.6693 11.6825 14.6693 8.00065C14.6693 4.31875 11.6845 1.33398 8.0026 1.33398C4.32071 1.33398 1.33594 4.31875 1.33594 8.00065C1.33594 11.6825 4.32071 14.6673 8.0026 14.6673Z"
					stroke="#A2A5C4"
					stroke-width="1.3"
					stroke-linecap="round"
					stroke-linejoin="round"
				/>
				<path
					d="M8 12.334V14.6673"
					stroke="#A2A5C4"
					stroke-width="1.3"
					stroke-linecap="round"
					stroke-linejoin="round"
				/>
				<path
					d="M12 8H14.6667"
					stroke="#A2A5C4"
					stroke-width="1.3"
					stroke-linecap="round"
					stroke-linejoin="round"
				/>
				<path
					d="M1.33594 8H3.66927"
					stroke="#A2A5C4"
					stroke-width="1.3"
					stroke-linecap="round"
					stroke-linejoin="round"
				/>
				<path
					d="M8 3.66732V1.33398"
					stroke="#A2A5C4"
					stroke-width="1.3"
					stroke-linecap="round"
					stroke-linejoin="round"
				/>
				<circle cx="8" cy="8" r="1" stroke="#A2A5C4" />
			</svg>
		</button>
	</div>
</div>

<style>
	label {
		display: block;
		width: 100%;
	}

	.tooltip {
		position: absolute;
	}

	.tooltip-inner {
		position: relative;
		left: -50%;
		padding: 2px 4px;
		font-size: 12px;
		color: #fff;
		background-color: #020c1a;
		border-radius: 4px;
	}

	.tooltip-inner::after {
		position: absolute;
		bottom: -3px;
		left: 50%;
		width: 6px;
		height: 6px;
		background-color: #020c1a;
		content: " ";
		transform: rotate(45deg);
		transform-origin: center center;
	}

	.atom-model-legend-container {
		position: absolute;
		top: 12px;
		right: 12px;
		display: flex;
		max-width: 200px;
		flex-wrap: wrap;
		gap: 8px 16px;
	}

	.atom-model-legend-item {
		display: flex;
		align-items: center;
		color: black;
	}

	.atom-model-legend-item-ball {
		margin-right: 8px;
		width: 8px;
		height: 8px;
		border-radius: 50%;
	}

	.material-viewer-container {
		width: 100%;
		height: 100%;
		position: relative;
		min-height: 240px;
	}

	.material-viewer-toolbar {
		position: absolute;
		right: 12px;
		top: 50%;
		transform: translateY(-50%);
		display: flex;
		flex-direction: column;
		color: #000000;

		background: #ffffff;
		box-shadow:
			0 6px 10px rgba(183, 192, 231, 0.1),
			0 8px 12px 1px rgba(170, 181, 223, 0.05);
		border-radius: 4px;
		padding: 4px;
		margin-bottom: 8px;
	}
	.material-viewer-toolbar-btn {
		cursor: pointer;
		font-size: 16px;
		height: 16px;
		width: 16px;
		margin-bottom: 4px;
	}
	.material-viewer-toolbar-btn:hover {
		cursor: pointer;
		color: #555878;
	}
	input {
		display: block;
		position: relative;
		outline: none !important;
		box-shadow: var(--input-shadow);
		background: var(--input-background-fill);
		padding: var(--input-padding);
		width: 100%;
		color: var(--body-text-color);
		font-weight: var(--input-text-weight);
		font-size: var(--input-text-size);
		line-height: var(--line-sm);
		border: none;
	}
	.container > input {
		border: var(--input-border-width) solid var(--input-border-color);
		border-radius: var(--input-radius);
	}
	input:disabled {
		-webkit-text-fill-color: var(--body-text-color);
		-webkit-opacity: 1;
		opacity: 1;
	}

	input:focus {
		box-shadow: var(--input-shadow-focus);
		border-color: var(--input-border-color-focus);
	}

	input::placeholder {
		color: var(--input-placeholder-color);
	}
</style>
