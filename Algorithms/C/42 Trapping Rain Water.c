int index_of_max_value(int left, int right, int* height)
{
    int max_value_index = left;
    for (int i = left + 1; i <= right; ++i){
        if (height[i] > height[max_value_index]){
            max_value_index = i;
        }
    }
    return max_value_index;
}

int sum(int left, int right, int* height)
{
    int s = 0;
    for (int i = left; i <= right; ++i){
        s += height[i];
    }
    return s;
}

// assume height[right] is the max value between [left, right]
int get_left_area(int left, int right, int* height)
{
    if (left >= right - 1){
        return 0;
    }

    // find the max value between [left, right - 1]
    int max_value_index = index_of_max_value(left, right - 1, height);
    if (height[max_value_index] == 0){
        return 0;
    }

    // caculate the area between [max_value_index + 1, right - 1]
    int area = height[max_value_index] * (right - 1 - (max_value_index + 1) + 1) - sum(max_value_index + 1, right - 1, height);
    return area + get_left_area(left, max_value_index, height);
}

// assume height[left] is the max value between [left, right]
int get_right_area(int left, int right, int* height)
{
    if (left >= right - 1){
        return 0;
    }

    // find the max value between [left + 1, right]
    int max_value_index = index_of_max_value(left + 1, right, height);
    if (height[max_value_index] == 0){
        return 0;
    }

    // caculate the area between [left + 1, max_value_index - 1]
    int area = height[max_value_index] * (max_value_index - 1 - (left + 1) + 1) - sum(left + 1, max_value_index - 1, height);
    return area + get_right_area(max_value_index, right, height);
}

int trap(int* height, int heightSize){
    if (height == NULL || heightSize == 0){
        return 0;
    }

    int max_value_index = index_of_max_value(0, heightSize - 1, height);
    if (height[max_value_index] == 0){
        return 0;
    }
    if (max_value_index == 0){
        return get_right_area(max_value_index, heightSize - 1, height);
    }
    if (max_value_index == heightSize - 1){
        return get_left_area(0, max_value_index, height);
    }
    return get_left_area(0, max_value_index, height) + get_right_area(max_value_index, heightSize - 1, height);
}
