**Requisitos**

- Entorno virtual `venv`.
- [Learn CSS](https://web.dev/learn/css)

**Dependencias**

- [Reflex](https://reflex.dev)
- requerimientos > `requirements.txt`

**Ejecucion**

- `reflex run`
- `reflex run --loglevel debug` _(modo debug)_

**Despliegue**

El script `build.sh` contiene las intrucciones necesarias para empaquetar el frontend del proyecto y deplegarlo de forma estatica. Este, en concreto, desde Vercel

`sh build.sh`

```sh
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -fr public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
```

