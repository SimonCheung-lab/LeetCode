int max(int a, int b)
{
    return a > b ? a : b;
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int maxArea(int* height, int heightSize){
    int area = 0;
    int left, right;
    left = 0;
    right = heightSize - 1;
    while (left < right) {
        area = max(area, min(height[left], height[right]) * (right - left));
        if (height[left] < height[right]) {
            ++left;
        }
        else {
            --right;
        }
    }
    return area;
}
