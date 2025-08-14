# SizeByAspectRatioProX
一个用于 ComfyUI 的自定义节点，根据宽高比和基础长度计算图像尺寸。A ComfyUI custom node for calculating image dimensions based on aspect ratio and base length.
# SizeByAspectRatioProX 节点

## 简介 (Introduction)

**SizeByAspectRatioProX** 是一个为 ComfyUI 设计的自定义节点，用于根据指定的宽高比和基础长度计算图像尺寸。它支持多种预设宽高比、自定义输入模式以及最大边界限制，适合需要精确控制图像尺寸的工作流。

**SizeByAspectRatioProX** is a custom node for ComfyUI designed to calculate image dimensions based on a specified aspect ratio and base length. It supports multiple preset aspect ratios, custom input modes, and maximum boundary limits, making it ideal for workflows requiring precise image size control.

---

## 功能特点 (Features)

- **多种宽高比预设**：支持常见的宽高比（如 1:1、4:3、16:9 等），并允许用户自定义宽高比。
- **灵活的输入模式**：支持以宽度、高度或长边为基准，自动计算另一维度。
- **最大边界限制**：确保输出的宽度和高度不超过用户定义的最大值。
- **强制偶数输出**：可选功能，确保输出的宽度和高度为偶数，适合特定图像处理需求。
- **多种输出类型**：提供宽度、高度、尺寸文本、宽高比浮点数、比例文本、长边、短边以及 BOX 格式输出，方便与其他节点集成。

- **Multiple Aspect Ratio Presets**: Supports common aspect ratios (e.g., 1:1, 4:3, 16:9) and allows custom aspect ratio input.
- **Flexible Input Modes**: Calculate dimensions based on width, height, or longest side.
- **Maximum Boundary Limits**: Ensures output width and height do not exceed user-defined maximums.
- **Force Even Output**: Optional feature to ensure width and height are even numbers, suitable for specific image processing needs.
- **Multiple Output Types**: Provides width, height, size text, aspect ratio float, ratio text, long side, short side, and BOX format outputs for easy integration with other nodes.

---

## 安装 (Installation)

1. **克隆或下载节点**：
   将本节点文件夹 `SizeByAspectRatioProX` 放入 ComfyUI 的自定义节点目录：ComfyUI/custom_nodes/SizeByAspectRatioProX/
   
2. **确保文件结构**：
确保文件夹包含以下文件：ComfyUI/custom_nodes/SizeByAspectRatioProX/
├── init.py
├── SizeByAspectRatioProX.py
├── README.md

3. **重启 ComfyUI**：
完全关闭 ComfyUI（包括后端服务），然后重新启动以加载节点。

4. **检查节点**：
在 ComfyUI 界面中，双击画布打开节点搜索框，输入 `Size By Aspect Ratio Pro X`，节点应出现在 `Utilities/SizeByAspectRatio` 分类下。

1. **Clone or Download the Node**:
Place the `SizeByAspectRatioProX` folder in ComfyUI's custom nodes directory:ComfyUI/custom_nodes/SizeByAspectRatioProX/

2. **Verify File Structure**:
Ensure the folder contains the following files:
ComfyUI/custom_nodes/SizeByAspectRatioProX/
├── init.py
├── SizeByAspectRatioProX.py
├── README.md

3. **Restart ComfyUI**:
Fully close ComfyUI (including the backend service) and restart to load the node.

4. **Check the Node**:
In the ComfyUI interface, double-click the canvas to open the node search, type `Size By Aspect Ratio Pro X`, and the node should appear under `Utilities/SizeByAspectRatio`.

---

## 使用方法 (Usage)

1. **添加节点**：
在 ComfyUI 画布中添加 `Size By Aspect Ratio Pro X` 节点（位于 `Utilities/SizeByAspectRatio`）。

2. **配置参数**：
- **base_preset**：选择预设宽高比（如 `1:1`、`16:9`），或选择 `Custom` 自定义宽高比。
- **input_mode**：选择计算模式（`Width`、`Height` 或 `Longest Side`）。
- **base_length**：设置基础长度（整数，范围 1-10000）。
- **aspect_ratio**：当选择 `Custom` 时，输入自定义宽高比（如 `1.78` 表示 16:9）。
- **max_width** 和 **max_height**：设置最大宽度和高度限制。
- **force_even**：启用以确保输出尺寸为偶数。

3. **连接输出**：
使用节点的输出（如 `width`、`height` 或 `box`）连接到其他节点以继续工作流。

1. **Add the Node**:
Add the `Size By Aspect Ratio Pro X` node to the ComfyUI canvas (found under `Utilities/SizeByAspectRatio`).

2. **Configure Parameters**:
- **base_preset**: Select a preset aspect ratio (e.g., `1:1`, `16:9`), or choose `Custom` for a custom ratio.
- **input_mode**: Choose the calculation mode (`Width`, `Height`, or `Longest Side`).
- **base_length**: Set the base length (integer, range 1-10000).
- **aspect_ratio**: Enter a custom aspect ratio (e.g., `1.78` for 16:9) when `Custom` is selected.
- **max_width** and **max_height**: Set maximum width and height limits.
- **force_even**: Enable to ensure output dimensions are even numbers.

3. **Connect Outputs**:
Use the node’s outputs (e.g., `width`, `height`, or `box`) to connect to other nodes in your workflow.

---

## 输出说明 (Output Description)

- **width (INT)**：计算后的宽度。
- **height (INT)**：计算后的高度。
- **size_text (STRING)**：格式化的尺寸文本（如 `1920x1080`）。
- **aspect_ratio_float (FLOAT)**：宽高比的浮点数表示。
- **ratio_text (STRING)**：宽高比的文本表示（如 `16:9`）。
- **long_side (INT)**：长边的像素值。
- **short_side (INT)**：短边的像素值。
- **box (BOX)**：包含 [x, y, width, height] 的边界框格式，x 和 y 默认为 0。

- **width (INT)**: Calculated width.
- **height (INT)**: Calculated height.
- **size_text (STRING)**: Formatted size text (e.g., `1920x1080`).
- **aspect_ratio_float (FLOAT)**: Aspect ratio as a floating-point number.
- **ratio_text (STRING)**: Aspect ratio as text (e.g., `16:9`).
- **long_side (INT)**: Pixel value of the longest side.
- **short_side (INT)**: Pixel value of the shortest side.
- **box (BOX)**: Bounding box format [x, y, width, height], with x and y defaulting to 0.

---

## 故障排除 (Troubleshooting)

- **节点未出现在 ComfyUI 菜单**：
- 确保文件结构正确，`__init__.py` 和 `SizeByAspectRatioProX.py` 存在且无语法错误。
- 检查 ComfyUI 日志（终端或 `ComfyUI/output` 文件夹），查找与 `SizeByAspectRatioProX` 相关的错误。
- 重启 ComfyUI，确保完全关闭后重新启动。
- 确保文件夹路径无中文或特殊字符。

- **输出尺寸不正确**：
- 检查 `base_length`、`max_width` 和 `max_height` 是否设置合理。
- 确保 `input_mode` 和 `base_preset` 匹配你的需求。

- **Node Not Appearing in ComfyUI Menu**:
- Verify the file structure is correct, with `__init__.py` and `SizeByAspectRatioProX.py` present and free of syntax errors.
- Check ComfyUI logs (terminal or `ComfyUI/output` folder) for errors related to `SizeByAspectRatioProX`.
- Restart ComfyUI, ensuring it is fully closed before restarting.
- Ensure the folder path contains no Chinese or special characters.

- **Incorrect Output Dimensions**:
- Verify that `base_length`, `max_width`, and `max_height` are set appropriately.
- Ensure `input_mode` and `base_preset` match your requirements.

---

## 贡献 (Contributing)

欢迎提交问题或建议！请通过 GitHub 或 ComfyUI 社区联系我们。

We welcome issues and suggestions! Please reach out via GitHub or the ComfyUI community.

---

## 许可证 (License)

本项目遵循 MIT 许可证。

This project is licensed under the MIT License.
