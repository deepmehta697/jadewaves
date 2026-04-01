from pathlib import Path

import generate_quartz_grits_q2_coa as base


base.OUTPUT = base.ROOT / "output" / "pdf" / "coa-quartz-grits-q2-premium-executive.pdf"
base.VECTOR_OUTPUT = base.ROOT / "tmp" / "pdfs" / "coa-quartz-grits-q2-executive-vector.pdf"
base.FLATTENED_IMAGE = base.ROOT / "tmp" / "pdfs" / "coa-quartz-grits-q2-executive-flattened.png"
base.DELIVERY_OUTPUT = Path("/Users/deepmehta/Documents/Jade Waves Enterprise/Products/Quartz/COA Quartz Grits Q2 - Premium Executive.pdf")
base.ASSET_OUTPUT = Path("/Users/deepmehta/Documents/Jade Waves Enterprise/Products/Quartz/assets/COA/all coas/COA Quartz Grits Q2 - Premium Executive.pdf")


if __name__ == "__main__":
    base.generate()
