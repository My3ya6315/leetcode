def triangle_type(nums: list[int]) -> str:
    side1, side2, side3 = nums
    if side1 + side2 <= side3 or side3 + side2 <= side1 or side1 + side3 <= side2:
        return "none"
    if side1 == side2 == nums[2]:
        return "equilateral"
    if side1 == side2 != side3 or side3 == side2 != side1 or side1 == side3 != side2:
        return "isosceles"
    if side1 != side2 != side3:
        return "scalene"
    return "none"

def main():
    print(triangle_type([4, 4, 4]))
    print(triangle_type([2, 4, 4]))
    print(triangle_type([1, 3, 4]))
    print(triangle_type([4, 3, 5]))

if __name__ == "__main__":
    main()