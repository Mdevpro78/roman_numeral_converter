rye_init_env:
	rye init -v --name roman_to_integer

rye_sync:
	rye sync

rye_pre_commit:
	rye run pre-commit run --all-files
