# ComfyUI ReSharpen
This is an Extension for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), which allows you to increase or decrease the amount of details generated during the Stable Diffusion pipeline.

> **ie.** This is not just a postprocessing filter

## How to Use
- Attach the **ReSharpen** node between `Empty Latent` and your `Sampler` node of choice
- Adjust the **details** slider:
    - **Positive** values cause the images to be noisy
    - **Negative** values cause the images to be blurry

> Values too large or small may cause the result to become distorted!

### Important:
- `Ancestral` samplers *(**eg.** `Euler a`)* do **not** work.
- The effect is "global," meaning if you want to disable it during other parts of the workflow *(**eg.** during `Hires. Fix`)*, you need to add another **ReSharpen** node and set the `details` to `0` again.

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
