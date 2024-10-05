def find_days_to_greater_packs(pack_counts):
    n = len(pack_counts)
    result = [0] * n
    stack = []  # استک برای نگهداری ایندکس‌های روزها

    for i in range(n):
        # در حالی که استک خالی نیست و تعداد بسته‌ها در روز فعلی بیشتر از تعداد بسته‌ها در روز بالای استک است
        while stack and pack_counts[i] > pack_counts[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx

        # اضافه کردن روز فعلی به استک
        stack.append(i)

    # چاپ نتیجه به صورت لیست از روزها
    print(" ".join(map(str, result)))


# ورودی
input_data = input().strip().split()
pack_counts = list(map(int, input_data))
find_days_to_greater_packs(pack_counts)
