install-poetry:
	pip install --upgrade pip
	curl -sSL https://install.python-poetry.org | python -

setup:
	rm -rf .venv
	python -m venv .venv && . .venv/bin/activate
	pip install --upgrade pip
	poetry install --no-root

compose-up:
	docker-compose --file elasticsearch/docker-compose.yaml up -d
	until curl -s -o /dev/null -f localhost:9200; do echo "Waiting..." >&2; sleep 3; done

compose-down:
	docker-compose --file elasticsearch/docker-compose.yaml down --remove-orphans

index-documents:
	sh ./elasticsearch/index_sample_documents.sh

run-driver1:
	poetry run python -m src.Driver1 ./src/input.txt

run-driver2:
	poetry run python -m src.Driver2 ./src/input.txt | jq

run-driver3:
	poetry run python -m src.Driver3 ./src/input.txt | jq

test:
	poetry run pytest $(TESTS)
