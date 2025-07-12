
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
if ! command -v conda &> /dev/null; then
    sudo apt update
    wget https://repo.anaconda.com/archive/Anaconda3-2025.06-0-Linux-x86_64.sh -O Anaconda3.sh
    bash Anaconda3.sh -b -p "$HOME/anaconda3"
    rm Anaconda3.sh
    export PATH="$HOME/anaconda3/bin:$PATH"


fi

eval "$(conda shell.bash hook)"



# Conda 환셩 생성 및 활성화
## TODO
conda create --name myenv python=3.11 -y
conda activate myenv



## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO
conda install -y mypy 





# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    number="${file%.py}"
    python3 "$file" < "../input/${number}_input" > "../output/${number}_output"



done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO

cd ..
mypy submission > "mypy_log.txt"





# conda.yml 파일 생성
## TODO
conda env export > conda.yml



# 가상환경 비활성화
## TODO
conda deactivate 



