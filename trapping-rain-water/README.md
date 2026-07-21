# 🌊 Trapping Rain Water

> A simple Python solution that calculates the total amount of rainwater trapped between elevations.


## 🌍 Original Task

In this problem, we want to calculate the volume of water trapped between terrain elevations.

You are given **n** integers representing the heights of these elevations. Your task is to determine the total amount of water that can be trapped between them after rainfall.

In the original illustration, the elevations are shown in **black**, while the trapped water is shown in **blue**. The input consists of a list of integers, each representing the height of an elevation.


## 📖 Description

Given a sequence of non-negative integers representing the heights of terrain elevations, determine how much rainwater can be trapped after rainfall.

Each integer represents the height of a vertical bar with a width of **1 unit**.

The goal is to calculate the **total volume of water** trapped between the elevations.

> The original illustration shows the terrain in **black** and the trapped water in **blue**.


## 💡 Idea

For every position (except the first and last):

1. Find the **highest elevation to the left**.
2. Find the **highest elevation to the right**.
3. The water above the current position is:

```text
min(max_left, max_right) - current_height
```

Then Add this value to the final answer.


## 🧮 Algorithm

```text
answer = 0

for each position i:
    left_max  = maximum height from start to i
    right_max = maximum height from i to end

    trapped_water = min(left_max, right_max) - height[i]
    answer += trapped_water

print(answer)
```


## 📥 Input

A single line containing space-separated integers representing the heights of the terrain.


## 📤 Output

A single integer representing the total volume of trapped rainwater.


## 📝 License

This project is intended for educational purposes.
