from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {relative_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


qa_module = load_module("qa_report", "all-in-one-ppt/scripts/qa_report.py")
validate_module = load_module("validate_plan", "all-in-one-ppt/scripts/validate_plan.py")


def base_plan() -> dict:
    return {
        "deck_title": "Contract test",
        "route": "create",
        "modifiers": [],
        "canvas": {"width": 13.333, "height": 7.5, "unit": "in"},
        "style": {},
        "assets": [],
        "slides": [
            {
                "slide_no": 1,
                "title": "A native title",
                "purpose": "Test the contract",
                "takeaway": "Semantic objects stay native.",
                "layout": "title-and-content",
                "objects": [
                    {
                        "id": "body",
                        "type": "text",
                        "content": "Editable body",
                        "materialization": "native",
                        "editable": True,
                        "bbox": {"x": 0.8, "y": 1.5, "w": 11.7, "h": 4.8},
                    }
                ],
            }
        ],
    }


class ContractTests(unittest.TestCase):
    def test_valid_native_plan_passes(self) -> None:
        errors: list[str] = []
        validate_module.validate_plan(base_plan(), errors)
        self.assertEqual(errors, [])
        self.assertEqual(qa_module.qa(base_plan())["status"], "pass")

    def test_rasterized_chart_without_reason_is_rejected(self) -> None:
        plan = base_plan()
        plan["slides"][0]["objects"][0] = {
            "id": "chart-as-image",
            "type": "chart",
            "content": {"labels": ["A"], "values": [1]},
            "materialization": "raster",
            "editable": False,
            "bbox": {"x": 0.8, "y": 1.5, "w": 11.7, "h": 4.8},
        }
        errors: list[str] = []
        validate_module.validate_plan(plan, errors)
        self.assertTrue(any("raster_reason" in error for error in errors))
        self.assertEqual(qa_module.qa(plan)["status"], "fail")

    def test_noncanonical_route_is_rejected(self) -> None:
        plan = base_plan()
        plan["route"] = "document_to_deck"
        plan["modifiers"] = ["editable", "imagegen"]
        errors: list[str] = []
        validate_module.validate_plan(plan, errors)
        self.assertTrue(any("route must be one of" in error for error in errors))
        self.assertTrue(any("unsupported modifier" in error for error in errors))

    def test_full_slide_content_image_is_blocked(self) -> None:
        plan = base_plan()
        plan["assets"] = [
            {
                "id": "generated-slide",
                "source": "imagegen",
                "kind": "illustration",
                "status": "ready",
                "path": "generated-slide.png",
                "prompt": "A complete presentation slide",
                "alt_text": "Flattened slide",
            }
        ]
        plan["slides"][0]["objects"][0] = {
            "id": "flattened-slide",
            "type": "image",
            "role": "content",
            "content": "generated-slide.png",
            "materialization": "raster",
            "editable": False,
            "replaceable": True,
            "asset_id": "generated-slide",
            "bbox": {"x": 0, "y": 0, "w": 13.333, "h": 7.5},
        }
        report = qa_module.qa(plan)
        self.assertEqual(report["status"], "fail")
        self.assertTrue(any("full-slide raster" in issue["issue"] for issue in report["issues"]))


if __name__ == "__main__":
    unittest.main()
