{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShellNoCC {
    name = "RSA breaker env";

    nativeBuildInputs = with pkgs.buildPackages; [
        python3
        openssl
    ];

    shellHook = ''
        python3 -m venv .venv
        source .venv/bin/activate
        pip install --upgrade pip
        pip install sympy pycryptodome
    '';
}