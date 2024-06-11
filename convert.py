# model: paddle to paddle-lite
from paddlelite.lite import *

#model_dir="D:/study/github/good/paddle/model/ch_ppocr_mobile_v2.0_det_slim_infer"
model_dir="D:/study/github/good/paddle/model/ch_ppocr_mobile_v2.0_cls_slim_infer"
#model_dir="D:/study/github/good/paddle/model/ch_ppocr_mobile_v2.0_rec_slim_infer"

# 1. 创建opt实例
opt=Opt()
# 2. 指定输入模型地址
opt.set_model_dir(model_dir)
# 3. 指定转化类型： arm、x86、opencl、npu
opt.set_valid_places("arm")
# 4. 指定模型转化类型： naive_buffer、protobuf
# 设置模型的输出类型，当前支持naive_buffer和protobuf两种格式，android/ios预测需要转化为naive_buffer
opt.set_model_type("naive_buffer")
# 4. 输出模型地址
opt.set_optimize_out(model_dir)
# 5. 执行模型优化
opt.run()
