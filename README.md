# ComfyUI ReSharpen
This is a Custom Node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), which allows you to increase or decrease the amount of details generated.

> **i.e.** This is not just a postprocessing filter

## How to Use
- Attach the **ReSharpen** node between `Empty Latent` and `KSampler` nodes
- Adjust the **details** slider as needed
    - **positive** = noisy
    - **negative** = blurry

> [!Important]
> `Ancestral` samplers *(**e.g.** `Euler a`)* do **not** work

> [!Important]
> The effects are "global." If you want to disable it during other parts of the workflow *(**e.g.** during `Hires. Fix`)*, you need to add another **ReSharpen** node and set the **details** to `0.0` again

## Examples

<table>
    <thead align="center">
        <tr>
            <th>Details</th>
            <th>-0.5</th>
            <th>0.0</th>
            <th>0.5</th>
        </tr>
    </thead>
    <tbody align="center">
        <tr>
            <td>Result</td>
            <td><img src="samples\-0.5.jpg" width=256></td>
            <td><img src="samples\0.0.jpg" width=256></td>
            <td><img src="samples\0.5.png" width=256></td>
        </tr>
    </tbody>
</table>

> [!Tip]
> The `0.5.png` contains Workflow

<hr>

- [How does it work?](https://github.com/Haoming02/sd-webui-resharpen/blob/main/README.md#how-does-it-work)
