from django.http import HttpResponse
from .tokenizer.scripts import vn_tokenizer

def index(request):
  vn_tokenizer.tokenize("thuan.txt", "haha.txt")
  return HttpResponse("Hello,e at the polls index.")

def remove(request):
  stopWords = ["nhận", "rằng", "cao", "nhà", "quá", "riêng", "gì", "muốn", "rồi", "số", "thấy", "hay", "lên", "lần",
        "nào", "qua", "bằng", "điều", "biết", "lớn", "khá", "vừa", "nếu", "thời gian", "họ", "từng", "đây", "tháng", "trước", "chính", "cả", "việc", "chưa", "do", "nói", "ra", "nên", "đều", "đi", "tới", "tôi", "có thể", "cùng", "vì", "làm", "lại", "mới", "ngày", "đó", "vẫn", "mình", "chỉ", "thì", "đang", "còn", "bị", "mà", "năm", "nhất", "hơn", "sau", "ông", "rất", "anh", "phải", "như", "trên", "tại", "theo", "khi", "nhưng", "vào", "đến", "nhiều", "người", "từ", "sẽ", "ở", "cũng", "không", "về","để","này","những","một","các","cho","được","với","có","trong","đã","là","và","của","thực sự","ở trên","tất cả","dưới", "hầu hết","luôn","giữa", "bất","kỳ","hỏi","bạn","cô","tôi","tớ","cậu","bác","chú","dì","thím","cậu","mợ","ông","bà","em", "thường", "ai","cảm ơn"]
  inputWords = ["nhận", "a", "rằng", "cao", "nhà", "b"]
  results = []
  # results.remove(element)
  for word in inputWords:
    if word.lower() not in stopWords:
      results.append(word)

  return HttpResponse(results)
