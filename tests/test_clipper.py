import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from helpers import mkdir
from clipper import make_clips 

from conf import TEST_DIR

if len(sys.argv) != 3:
    print("test_clipper.py <video> <input-file>")
    exit(1)

CLIPPER_OUTPUT_DIR = TEST_DIR + "./clipper_output"
mkdir(CLIPPER_OUTPUT_DIR)
TEST_VIDEO = sys.argv[1]
TEST_INPUT = sys.argv[2]


def test_make_clips():
    res = make_clips(video_file=TEST_VIDEO, input_file=TEST_INPUT, output_dir=CLIPPER_OUTPUT_DIR, lower_bound=5.0, upper_bound=15.0, debug_flag1=True)
    assert len(res) != 0
    
