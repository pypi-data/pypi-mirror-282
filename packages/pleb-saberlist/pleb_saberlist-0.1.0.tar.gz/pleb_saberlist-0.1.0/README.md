# playlist helper

## Development

Clone the repo and install dependencies into a local virtual environment:

```bash
pip install --upgrade pip
pip install --editable .
```

## Resources

* [Beatleader API](https://beatleader.xyz/developer)
* [ScoreSaber API](https://docs.scoresaber.com/)

## Tips

Avoid printing covers in console.

```shell
jq 'del(.image)' < playlist.bplist
```
