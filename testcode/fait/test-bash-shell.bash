#!/bin/bash
# Bash Example
PI=3.141592653589793
radius=5

area=$(echo "$PI * $radius^2" | bc -l)
perimeter=$(echo "2 * $PI * $radius" | bc -l)

echo "Area: $area"
echo "Perimeter: $perimeter"
