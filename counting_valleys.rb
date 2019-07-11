#!/bin/ruby
# frozen_string_literal: true

# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

# For example, if Gary's path is , he first enters a valley units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

# Function Description

# Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

# countingValleys has the following parameter(s):

# n: the number of steps Gary takes
# s: a string describing his path
require 'pry'

# Complete the countingValleys function below.
def countingValleys(_n, s)
  array = s.split('')
  altitude = 0
  valleys = 0
  # start at sea level. If there is a step up
  # add 1 to altitude. If there is a step down
  # minus 1 from altitude.
  # if there was a step down from 0, altitude will equal -1
  # if there was a second step down, altitude will equal -2
  # if there is a step up now, altitude will equal -1
  # if there is another step up, valleys will equal to 1,
  # altitude will equal to 0.
  array.each do |step|
    if step == 'U'
      valleys += 1 if altitude == -1
      altitude += 1
    end
    altitude -= 1 if step == 'D'
  end
  valleys
end
