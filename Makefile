install : 
	pip install -r requirements.txt

run : 
	streamlit run src/home.py

compose :
	@echo "Composing up docker"
	docker compose up 

	
build :	
	@echo "docker build -t counter_app ."
	docker build -t counter_app .

	
