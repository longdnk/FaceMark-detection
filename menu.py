import subprocess

MODEL_FILE="detect_mask_video.py"

def test():
    print("Test Env OK")

def runModel():
    try:
        subprocess.run(["python3.7", MODEL_FILE], check=True)
    except subprocess.CalledProcessError as e:
        print("SOME ERROR OCCURRED", e)

def default():
    print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

def main():
    menu = {
        '1': test,
        '2': runModel,
        '3': exit
    }

    while True:
        print("\nMasked System:")
        print("1. Test Info")
        print("2. Run Model")
        print("3. Exit")

        choice = input("Nhập lựa chọn của bạn: ")
        menu.get(choice, default)()

if __name__ == "__main__":
    main()