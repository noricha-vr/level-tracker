import pandas as pd
import matplotlib.pyplot as plt
import os


def plot_decibel_levels(csv_path, output_filename=None, output_dir='output', skiprows=4, encoding='cp932'):
    """
    Reads the specified CSV file, plots decibel levels over time, and saves the plot.
    
    Parameters:
    - csv_path: Path to the CSV file.
    - output_filename: Name for the output plot file (default: derived from csv_path).
    - output_dir: Directory to save the plot (default: 'output').
    - skiprows: Number of rows to skip before the header (default 4).
    - encoding: File encoding (default 'cp932' for Shift_JIS).
    """
    # CSV読み込み
    df = pd.read_csv(csv_path, skiprows=skiprows, encoding=encoding)

    # 列名の前後空白を削除
    df.columns = df.columns.str.strip()

    # アドレス列があれば削除
    if 'ｱﾄﾞﾚｽ' in df.columns:
        df = df.drop(columns=['ｱﾄﾞﾚｽ'])

    # 数値列を抽出
    num_cols = df.select_dtypes(include='number').columns

    # インデックスを10分割して秒に変換（1秒間に10サンプル）
    time_s = df.index / 10.0

    # プロット
    plt.figure(figsize=(10, 6))
    for col in num_cols:
        plt.plot(time_s, df[col], label=col)
    plt.xlabel('Time (s)')
    plt.ylabel('Level (dB)')
    plt.title(f'Decibel Levels Over Time - {os.path.basename(csv_path)}')
    plt.legend(loc='upper right', fontsize='small', ncol=2)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    # Generate output filename if not provided
    if output_filename is None:
        base_name = os.path.basename(csv_path)
        file_name_without_ext = os.path.splitext(base_name)[0]
        output_filename = f"{file_name_without_ext}.png"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the plot
    output_path = os.path.join(output_dir, output_filename)
    plt.savefig(output_path)
    print(f"Plot saved to: {output_path}")
    plt.close()


if __name__ == '__main__':
    import sys
    # デフォルトのCSVパスを設定
    default_csv_path = 'test.csv'
    csv_path = sys.argv[1] if len(sys.argv) > 1 else default_csv_path

    # プロット関数を呼び出し、出力ファイル名を渡す (ファイル名は関数内で生成される)
    plot_decibel_levels(csv_path) # Call function without output_filename, it will be generated inside
