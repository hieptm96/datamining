def remove_stop_words(inputWords):
  stopWords1 = ['nhận', 'rằng', 'cao', 'nhà', 'quá', 'riêng', 'gì', 'muốn', 'rồi', 'số', 'thấy', 'hay', 'lên', 'lần',
        'nào', 'qua', 'bằng', 'điều', 'biết', 'lớn', 'khá', 'vừa', 'nếu', 'thời gian', 'họ', 'từng', 'đây', 'tháng', 'trước',
        'chính', 'cả', 'việc', 'chưa', 'do', 'nói', 'ra', 'nên', 'đều', 'đi', 'tới', 'tôi', 'có thể', 'cùng', 'vì', 'làm', 'lại',
        'mới', 'ngày', 'đó', 'vẫn', 'mình', 'chỉ', 'thì', 'đang', 'còn', 'bị', 'mà', 'năm', 'nhất', 'hơn', 'sau', 'ông', 'rất',
        'anh', 'phải', 'như', 'trên', 'tại', 'theo', 'khi', 'nhưng', 'vào', 'đến', 'nhiều', 'người', 'từ', 'sẽ', 'ở', 'cũng',
        'không', 'về','để','này','những','một','các','cho','được','với','có','trong','đã','là','và','của','thực_sự','ở_trên','tất_cả','dưới', 'hầu_hết','luôn','giữa', 'bất','kỳ','hỏi','bạn','cô','tôi','tớ','cậu','bác','chú','dì','thím','cậu','mợ','ông','bà','em', 'thường', 'ai','cảm_ơn']
  stopWords2 = ['bị', 'bởi', 'cả', 'các', 'cái', 'cần', 'càng', 'chỉ', 'chiếc', 'cho', 'chứ', 'chưa', 'chuyện', 'có',
  'có_thể', 'cứ', 'của', 'cùng', 'cũng', 'đã', 'đang', 'đây', 'để', 'đến_nỗi', 'đều', 'điều', 'do', 'đó', 'được', 'dưới',
  'gì', 'khi', 'không', 'là', 'lại', 'lên', 'lúc', 'mà', 'mỗi', 'một_cách', 'này', 'nên', 'nếu', 'ngay', 'nhiều', 'như',
  'nhưng', 'những', 'nơi', 'nữa', 'phải', 'qua', 'ra', 'rằng', 'rằng', 'rất', 'rất', 'rồi', 'sau', 'sẽ', 'so', 'sự', 'tại',
  'theo', 'thì', 'trên', 'trước', 'từ', 'từng', 'và', 'vẫn', 'vào', 'vậy', 'vì', 'việc', 'với', 'vừa']
  stopWords = list(set(stopWords1 + stopWords2))
  results = []
  # results.remove(element)
  for word in inputWords:
    if word.lower() not in stopWords:
      results.append(word)

  return results
