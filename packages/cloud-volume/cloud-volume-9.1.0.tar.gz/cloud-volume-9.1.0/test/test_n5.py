import pytest

import sys

import numpy as np

from cloudvolume import CloudVolume

def test_n5():
  image = np.random.randint(0,255, size=[101,102,103], dtype=np.uint8)

  vol = CloudVolume.from_numpy(
    image, "n5://file:///tmp/removeme/n5test",
  )













