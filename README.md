# ComfyUI ReSharpen
This is an Extension for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), which allows you to increase or decrease the amount of details of the generation during the Stable Diffusion pipeline.

> **ie.** This is not just a postprocessing filter

## How to Use
- Attach the **ReSharpen** node between `Empty Latent` and `KSampler` nodes
- Adjust the **details** slider:
    - **Positive** values cause the images to be noisy
    - **Negative** values cause the images to be blurry

> Don't use values too close to `1` or `-1`, as it will become distorted

### Important:
- `Ancestral` samplers *(**eg.** `Euler a`)* do **not** work.
- The **enable** is "global." If you want to disable it during later part of the workflow *(**eg.** during `Hires. Fix`)*, 
you have to add another **ReSharpen** node and set it to disable.

## Examples

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
