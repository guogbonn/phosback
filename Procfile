web: echo "$(ls -l)" ;echo "$(pwd)"; cd core; python3 ping.py & ; uvicorn main:app --host=0.0.0.0 --port=${PORT:-8000} --workers=2; 
