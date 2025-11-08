"""Runner de demos para scripts 020..024

Este script ejecuta los demos no interactivos de los módulos externos y guarda
la salida en archivos dentro de `tests/outputs/`.

Uso:
  python tests/run_demos_020_024.py        # corre todos los demos sin paso interactivo
  python tests/run_demos_020_024.py --step # intenta ejecutar con la opción --step (requiere interacción manual)

Nota: los scripts usan prompts cuando se ejecutan con `--step`; este runner
no simula respuestas. Para pruebas no interactivas usa el modo por defecto.
"""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "020-external_straight_merging.py",
    "021-external_natural_merging.py",
    "022-balanced_multiway.py",
    "023-polyphase.py",
    "024-distribution_initial_runs.py",
]

OUT_DIR = ROOT / "tests" / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def run_script(fname: str, args: list[str]) -> tuple[int, str, str]:
    path = ROOT / fname
    cmd = [sys.executable, str(path)] + args
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def main():
    step_mode = "--step" in [a.lower() for a in sys.argv[1:]]
    for s in SCRIPTS:
        args: list[str] = []
        # algunos scripts aceptan 'demo' para modo ejemplo
        if s in ("020-external_straight_merging.py", "021-external_natural_merging.py"):
            args.append('demo')
        # para 022..024 no necesitan 'demo' pero aceptan --step para pausas
        if step_mode:
            args.append('--step')

        print(f"Ejecutando {s} {' '.join(args)}")
        code, out, err = run_script(s, args)
        out_file = OUT_DIR / (s.replace('.py', '') + ("_step" if step_mode else "") + ".txt")
        with out_file.open('w', encoding='utf-8') as f:
            f.write(f"# Command: {sys.executable} {s} {' '.join(args)}\n# Return code: {code}\n\n")
            f.write(out)
            if err:
                f.write('\n# STDERR:\n')
                f.write(err)
        print(f"  -> salida guardada en {out_file} (rc={code})")

    print("\nEjecución completada. Revisa los archivos en tests/outputs/ para ver las salidas.")


if __name__ == '__main__':
    main()
