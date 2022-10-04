#4

video_NVIDIA = [3070, 2060, 3090, 3070, 3090]
print("Количество видеокарт: ", len(video_NVIDIA))
max_value = max(video_NVIDIA)
new_array_video_NVIDIA = []
for i in range(len(video_NVIDIA)):
    print(f"{i + 1} Видеокарта:", video_NVIDIA[i])
    if video_NVIDIA[i] != max_value:
        new_array_video_NVIDIA .append(video_NVIDIA[i])
print("Старый список видеокарт:", video_NVIDIA)
print("Новый список видеокарт:", new_array_video_NVIDIA)
