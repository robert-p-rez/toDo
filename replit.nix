{ pkgs }: {
  deps = [
    pkgs.python311
  ];

  env = {
    PYTHONUNBUFFERED = "1";
  };

  setup = ''
    python3.11 -m ensurepip
    python3.11 -m pip install --upgrade pip
    pip install -r requirements.txt
  '';
}