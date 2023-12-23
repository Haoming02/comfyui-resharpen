# ComfyUI ReSharpen
This is an Extension for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), which allows you to increase or decrease the amount of details of the generation during the Stable Diffusion pipeline.

> **ie.** This is not just a postprocessing filter

## Nodes
- **Hook ReSharpen:** Hooks the callback to enable the effects. Comes with a **details** slider:
    - **Positive** values cause the images to be noisy
    - **Negative** values cause the images to be blurry

> Though, don't actually use values too close 1 or -1 as it will become distorted

- **Unhook ReSharpen** (Optional)**:** Unhook the callback to disable the effects.
    - If used, put near the end of the workflow

#### Important:
- `Ancestral` samplers *(**eg.** `Euler a`)* do **not** work.
- In a single workflow, you only need to hook the callback once. The simplest way is to add it between the `Positive Prompt` and the `Sampler`.
- Due to how `ComfyUI` works, if you also add **Unhook ReSharpen**, the effect may not work sometimes unless you also change the prompt.

> ComfyUI doesn't go through a node unless it needs to be updated, so if you unhook the callback and the parameters didn't change *(**eg.** you're only iterating throguh seeds)*, then the callback will not be hooked again. Easiest way to solve this is just adding a space to the positive prompt, or just don't unhook the callback.

## Samples

<table>
    <thead align="center">
        <tr>
            <td>Sharpness</td>
            <td><b>-0.5</b></td>
            <td><b>0.0</b></td>
            <td><b>0.5</b></td>
        </tr>
    </thead>
    <tbody align="center">
        <tr>
            <td>Result</td>
            <td><img src="samples\-0.5.jpg" width=256></td>
            <td><img src="samples\0.0.jpg" width=256></td>
            <td><img src="samples\0.5.jpg" width=256></td>
        </tr>
    </tbody>
</table>

<hr>

- [How does it work?](https://github.com/Haoming02/sd-webui-resharpen/blob/main/README.md#how-does-it-work)
