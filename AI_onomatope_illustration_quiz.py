import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import random
import diffusers

#語句ランダム
def random_word(word_list):
    select_word = random.choice(word_list)
    return select_word

class QuizApp:
    def __init__(self, master, word_list):
        self.master = master
        self.master.title("オノマトペイラストクイズアプリ")
        self.master.geometry("600x600")

        # クイズの問題と選択肢
        self.questions = []

        # 画像生成
        self.current_prompt_word = random_word(word_list)
        self.generate_image()

        # クイズUIの作成
        self.create_ui()

    # 画像生成
    def generate_image(self):
        pipe = diffusers.StableDiffusionPipeline.from_pretrained("Linaqruf/anything-v3.0")
        result = pipe(prompt=self.current_prompt_word, width=256, height=256, num_inference_steps=10)
        result.images[0].save("generated_image.png")

    # 画像表示
    def create_ui(self):
        self.image_label = tk.Label(self.master)
        self.image_label.pack(pady=10)

        # 問題文表示
        self.question_label = tk.Label(self.master, text="", font=("Nirmala UI", 12))
        self.question_label.pack(pady=10)

        # 選択肢ボタン
        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.choice_buttons.append(button)

        # 「次の問題へ」ボタン
        self.next_question_button = tk.Button(self.master, text="次の問題へ", command=self.show_next_question, bg="chocolate1", font=("Arial", 14, "bold"))
        self.next_question_button.place(x=400,y=500)

        # 「ゲームを終了」ボタン
        self.exit_quiz = tk.Button(self.master, text="ゲームを終了", command=self.exit_quiz, font=("Arial", 14, "bold"))
        self.exit_quiz.place(x=100,y=500)

        # クイズの開始
        self.show_question()

    def show_question(self):
        # 現在のクイズの情報を取得
        current_question_info = {
            "question": f"画像のお題は何でしょう？",
            "choices": [self.current_prompt_word],
            "correct_choice": self.current_prompt_word,
            "画像のパス": "generated_image.png"
        }

        # 選択肢に正解以外の語句を追加
        choices_pool = [word for word in word_list if word != current_question_info["correct_choice"]]
        current_question_info["choices"] += random.sample(choices_pool, 3)

        # ランダムに並び替え
        random.shuffle(current_question_info["choices"])

        # 画像を表示
        image_path = current_question_info["画像のパス"]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # 画像が参照され続けるようにする

        # 問題文と選択肢を表示
        self.question_label.config(text=current_question_info["question"])
        for i in range(4):
            self.choice_buttons[i].config(text=current_question_info["choices"][i])

        # 次の問題ボタン無効化
        self.next_question_button.config(state=tk.DISABLED)

    def check_answer(self, choice):
        # 正誤チェック
        current_question_info = {
            "correct_choice": self.current_prompt_word
        }

        if self.choice_buttons[choice].cget("text") == current_question_info["correct_choice"]:
            messagebox.showinfo("正解", "正解です！")
        else:
            messagebox.showinfo("不正解", f"不正解です。正解は {current_question_info['correct_choice']} でした。")

        # 次の問題ボタン有効化
        self.next_question_button.config(state=tk.NORMAL)

    #次の問題
    def show_next_question(self):
        self.current_prompt_word = random_word(word_list)

        # 画像生成
        self.generate_image()

        # 次の問題に進む
        self.show_question()

    #クイズ終了
    def exit_quiz(self):
        self.master.destroy()

if __name__ == "__main__":
    # 単語リスト
    word_list = ["kirakira", "fuwafuwa", "gizagiza", "meramera"]

    # アプリ起動
    root = tk.Tk()
    app = QuizApp(root, word_list)
    root.mainloop()
