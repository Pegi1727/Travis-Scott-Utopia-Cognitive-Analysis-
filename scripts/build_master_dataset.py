import pandas as pd
import os

output_excel = "[/mnt/data/Utopia_MMM_Replication_Package.xlsx"](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwNzN0KgjAYANB32XWT5ZS2bsOSYhSBlBCMr23qcvmTS6To3fMBzvmi92BeaI3GMIA02_gk0vya5kd3yLmodjhNSDWqT-2ejx7vLxy3tBeKbVdlghZIVeClb2vTzMW9iEDFmmBNWIwjyhgGRinmRPFQG7rUoGdTWGdkB76aSebbzoIUQsiz6ZxV4G3byBOoGkoTTG6Ybgj9_uMwNSQ:1xLunK:VWVvYbPqOy3KCRZDlmUYeIt18Hwx1x97fYTpkfUI6MU/Utopia_MMM_Replication_Package.xlsx%22)

csv_mapping = {
    "Track_Summary": "[/mnt/data/mmm_track_summary_reconstructed.csv"](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwNzNEKgjAUANB_2XOT5ZS2XsOSQnqKEoJxu5utdJpzChX9e37AOV8yDsaTNZniCPLTJmSJlpe8PDaHUhZ2R_OM2Qk_deOePd2fJe14X6DYru4ZWRC0EFToatPOxa1KAFPNqGYipQkXgoLgnEqGMtaGLzXo2VSPxqgXBDsT55wKHrBWw-gc-LfyBrt2CH7EYHSEw3Ql5PcH_CA2EQ:1xLunK:E3fEt8GBzTlssg2ikvYpCDZR4f4RbYwuQKrgRe7FMv8/mmm_track_summary_reconstructed.csv%22),
    "Schema_Table": "[/mnt/data/mmm_schema_table_reconstructed.csv"](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwNzEELgjAYgOH_snOT5ZS2rmFJIZ2ihEA-v81WOk03PRT993Z94Xm_ZHZ6IluyxBHkl53PEiVveXnuTqUszIHmGTMLftrOvkZ6vEo68LFAsd88MrIiaMBXfmh1HxZ1kwCmilHFREoTLgQFwTmVDGWsNF8rUME0z05Xb_AmEGtt5dBoC5WHOvRJ49A7P83otYrQLXdCfn--7jVn:1xLunK:e0QAysKWarlMsndNz0wPy3_PO2WjdsrXwP3DUheYshM/mmm_schema_table_reconstructed.csv%22),
    "Acoustic_Cognitive": "[/mnt/data/acoustic_cognitive_correspondence_reconstructed.csv"](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwNzLEOgjAUQNF_6WwJWoitq0GJhjgZJTEh9fVBEWyhLQwa_122u5z7JZNHR3Zk3kQyv-5Dlihxz8tLfy5FoY80z2I9w6fr36-Rnm6CWjYWwA_bJiMrAlqGKtgOzbJ41omEVMVUxTylCeOcSs4YFTGIjUK2VlItpm57rAYZ9EIk2MmHFiqwjWlDO-NSzqEfrFFoACuHYI0PboKAKgI_Pwj5_QGdlzyk:1xLunK:5hVOx2BtPtH11cdZ7d7tvbeCqGazHm_Jbqc-fZX0U80/acoustic_cognitive_correspondence_reconstructed.csv%22),
    "Reliability": "[/mnt/data/reliability_report_reconstructed.csv"](https://gapgpt.app/api/v1/code_interpreter/v2.aHUCtE4d9XHYOlKY9MhG-HE0hvczklmjq-JW9-o3qMc8F7gE/bf4ac5d0-d085-4388-a833-90c92de31dad/.eJwNzEELgjAYgOH_snOT5ZS2rmFJIZ2ihEDmNpu5nM5PoaL_3k7v6Xm_aJ60R1u0xJHILzvIEsVveXm2p5IX5oDzjJhFfjr7eo74eOXY0bGQbL95ZGiFpBFQget0HxZ1kwiZKoIVYSlOKGNYMEoxJ5LHStO1EiqYprW6GgSYQLy2rahb28K78npwHkKk6yfwswStIjktd4R-fzMyNn4:1xLunK:btaBRnCL6ZzzHeS0qunML-C1dLoNhbkk5QLQVhxPJig/reliability_report_reconstructed.csv%22)
}

with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
    for sheet_name, file_path in csv_mapping.items():
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Added sheet: {sheet_name}")

print(f"Master replication package built successfully: {output_excel}")
