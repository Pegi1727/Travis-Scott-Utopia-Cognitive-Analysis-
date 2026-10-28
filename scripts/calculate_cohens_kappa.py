import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score, confusion_matrix

# شبیه‌سازی مشاهدات تطبیق‌یافته دو کدگذار بر اساس ۴ بعد تحلیلی در پروتکل
categories = ['CONTAINER', 'FORCE', 'PATH', 'VERTICALITY', 'BALANCE']

# نمونه کدهای ثبت‌شده فرضی دو ارزیاب روی ۶۰ بخش متنی-صوتی
np.random.seed(42)
rater1 = np.random.choice(categories, size=60, p=[0.25, 0.30, 0.20, 0.15, 0.10])
rater2 = rater1.copy()
# اعمال اختلاف‌های جزئی برای رسیدن به کاپای حدود ۰.۸۴
disagree_idx = np.random.choice(range(60), size=6, replace=False)
for idx in disagree_idx:
    rater2[idx] = np.random.choice([c for c in categories if c != rater1[idx]])

kappa = cohen_kappa_score(rater1, rater2)
print(f"Calculated Inter-Rater Reliability (Cohen's Kappa): {kappa:.3f}")

conf_mat = pd.DataFrame(
    confusion_matrix(rater1, rater2, labels=categories),
    index=[f"Rater1_{c}" for c in categories],
    columns=[f"Rater2_{c}" for c in categories]
)
conf_mat.to_csv("[/mnt/data/inter_rater_confusion_matrix.csv"](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwVzEELgjAYgOH_snOT5ZS2rmFJIZ2ihEC-ttmWuuWcEkX_Pbu8t-f9oHFQHq3RFEeQnzYhSyS_5OWxPZS80DucZ0RP4t203aPH-zPHjvaFYNvVPUMLJDSEKrhG2XlxqxMQqSRYEpbihDKGgVGKORE8loouJcjZ1KZV1ROCnomxQfnKw7_C2XocjLNVB8GbVySG6YrQ9wdYdDTL:1xLunJ:cWwzuzMMxHt6dESfSLsjd_0jfD8RlCnKrkccb-0TsKw/inter_rater_confusion_matrix.csv%22))
print("Confusion matrix saved to inter_rater_confusion_matrix.csv")
