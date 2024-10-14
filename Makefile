rye_init_env:
	rye init -v --name roman_to_integer

rye_sync:
	rye sync

rye_pre_commit:
	rye run pre-commit run --all-files -v --color always

rye_run_tests:
	rye run pytest -n 2 -q tests/conversion/

rye_run_server:
	rye run uvicorn src.main:app --reload --port 8080

dupd:
	docker compose -f docker-compose.yaml up -d

dbuild:
	docker compose -f docker-compose.yaml build --no-cache

dbuildrm:
	docker image rm roman-conveter:latest

ddownv:
	docker compose -f docker-compose.yaml down -v

dlogsf:
	docker compose -f docker-compose.yaml logs -f

dpsa:
	docker compose -f docker-compose.yaml ps -a

dupdtests:
	docker compose -f docker-compose.yaml -f docker-compose.test.yaml up -d

druntest:
	docker compose -f docker-compose.yaml -f docker-compose.test.yaml exec -it backend sh -c "dos2unix /app/scripts/run_tests.sh && /app/scripts/run_tests.sh"
