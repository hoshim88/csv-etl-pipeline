import pandas as pd

def main():
    df = pd.read_csv("people.csv")

    filtered = df[df["age"] > 26]
    filtered.to_csv("people_over_26.csv", index=False)

    print("Saved people_over_26.csv")
    print("Rows:", len(filtered))

if __name__ == "__main__":
    main()
