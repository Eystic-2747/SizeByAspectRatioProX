# SizeByAspectRatioProX.py
# 豪华扩展版 - 带尺寸预设 / 最大边界 / 偶数强制 / BOX 输出
import math

PHI = (1 + 5 ** 0.5) / 2
SQRT2 = 2 ** 0.5

def _ceil_to_multiple(x: float, m: int) -> int:
    return int(math.ceil(max(1.0, x) / m) * m)

def _floor_to_multiple(x: float, m: int) -> int:
    return int(math.floor(max(1.0, x) / m) * m)

def _round_to_multiple(x: float, m: int) -> int:
    return int(round(max(1.0, x) / m) * m)

def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

def _ratio_text(w: int, h: int) -> str:
    g = _gcd(w, h)
    return f"{w//g}:{h//g}"

class SizeByAspectRatioProX:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        ratio_list = [
            "1:1", "1:2", "2:1", "3:2", "2:3", "4:3", "3:4",
            "5:4", "4:5", "16:9", "9:16", "21:9", "9:21",
            "2.39:1", "1:2.39",
            "golden_horizontal", "golden_vertical",
            "sqrt2_horizontal", "sqrt2_vertical",
            "custom"
        ]
        input_mode_list = [
            "longest", "shortest", "width", "height",
            "total_pixels_kpx", "total_pixels_mpx",
        ]
        rounding_mode_list = ["nearest", "ceil", "floor", "none"]
        base_presets = ["custom", "512", "768", "1024", "1536", "2048", "3072", "4096"]

        return {
            "required": {
                "base_preset": (base_presets,),
                "base_length": ("INT", {"default": 1000, "min": 1, "max": 100000, "step": 1}),
                "input_mode": (input_mode_list,),
                "aspect_ratio": (ratio_list,),
                "round_to_multiple": ("INT", {"default": 8, "min": 1, "max": 1024, "step": 1}),
                "rounding_mode": (rounding_mode_list,),
                "max_side_limit": ("INT", {"default": 4096, "min": 1, "max": 100000, "step": 1}),
                "force_even": ("BOOLEAN", {"default": False}),
                "custom_width": ("FLOAT", {"default": 1.0, "min": 0.001, "max": 10000.0, "step": 0.001}),
                "custom_height": ("FLOAT", {"default": 1.0, "min": 0.001, "max": 10000.0, "step": 0.001}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "STRING", "FLOAT", "STRING", "INT", "INT", "BOX")
    RETURN_NAMES = ("width", "height", "size_text", "aspect_ratio_float", "ratio_text", "long_side", "short_side", "box")
    FUNCTION = "calc_size"
    CATEGORY = "Utilities/SizeByAspectRatio"

    def _parse_ratio(self, aspect_ratio: str, cw: float, ch: float) -> float:
        if aspect_ratio == "custom":
            return float(cw) / float(ch)
        if aspect_ratio == "golden_horizontal":
            return PHI
        if aspect_ratio == "golden_vertical":
            return 1.0 / PHI
        if aspect_ratio == "sqrt2_horizontal":
            return SQRT2
        if aspect_ratio == "sqrt2_vertical":
            return 1.0 / SQRT2
        if ":" in aspect_ratio:
            w, h = aspect_ratio.split(":")
            return float(w) / float(h)
        return 1.0

    def _apply_rounding(self, w: float, h: float, multiple: int, mode: str):
        if mode == "none" or multiple <= 1:
            return int(round(w)), int(round(h))
        if mode == "ceil":
            return _ceil_to_multiple(w, multiple), _ceil_to_multiple(h, multiple)
        if mode == "floor":
            return _floor_to_multiple(w, multiple), _floor_to_multiple(h, multiple)
        return _round_to_multiple(w, multiple), _round_to_multiple(h, multiple)

    def _force_even_dims(self, w: int, h: int):
        if w % 2 != 0:
            w += 1
        if h % 2 != 0:
            h += 1
        return w, h

    def _apply_max_limit(self, w: int, h: int, max_side: int):
        if max(w, h) > max_side:
            scale = max_side / float(max(w, h))
            w = int(round(w * scale))
            h = int(round(h * scale))
        return w, h

    def calc_size(self, base_preset, base_length, input_mode, aspect_ratio,
                  round_to_multiple, rounding_mode, max_side_limit, force_even,
                  custom_width, custom_height):

        if base_preset != "custom":
            base_length = int(base_preset)

        r = self._parse_ratio(aspect_ratio, custom_width, custom_height)
        r = max(r, 1e-8)

        if input_mode == "width":
            width, height = float(base_length), base_length / r
        elif input_mode == "height":
            height, width = float(base_length), base_length * r
        elif input_mode == "longest":
            if r >= 1.0:
                width, height = float(base_length), base_length / r
            else:
                height, width = float(base_length), base_length * r
        elif input_mode == "shortest":
            if r >= 1.0:
                height, width = float(base_length), base_length * r
            else:
                width, height = float(base_length), base_length / r
        elif input_mode == "total_pixels_kpx":
            total = base_length * 1000.0
            width = math.sqrt(total * r)
            height = width / r
        elif input_mode == "total_pixels_mpx":
            total = base_length * 1_000_000.0
            width = math.sqrt(total * r)
            height = width / r
        else:
            width, height = float(base_length), base_length / r

        width, height = self._apply_rounding(width, height, int(round_to_multiple), rounding_mode)
        width, height = self._apply_max_limit(width, height, max_side_limit)
        if force_even:
            width, height = self._force_even_dims(width, height)

        size_text = f"{width}x{height}"
        aspect_ratio_float = width / max(1, height)
        ratio_text = _ratio_text(width, height)
        long_side, short_side = max(width, height), min(width, height)
        box = [0, 0, width, height]

        return (width, height, size_text, aspect_ratio_float, ratio_text, long_side, short_side, box)

NODE_CLASS_MAPPINGS = {
    "SizeByAspectRatioProX": SizeByAspectRatioProX
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SizeByAspectRatioProX": "Size By Aspect Ratio Pro X"
}