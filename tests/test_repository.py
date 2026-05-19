import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]

def test_skill_index_has_30_skills():
    index=json.loads((ROOT/'skills-index.json').read_text())
    assert len(index)==30
    assert all(item.get('production_ready') for item in index)

def test_every_skill_has_manifest_and_sample():
    for item in json.loads((ROOT/'skills-index.json').read_text()):
        skill=ROOT/item['path']
        assert skill.exists()
        assert (skill.parent/'skill.json').exists()
        assert (skill.parent/'sample-input.json').exists()
        assert '## Production contract' in skill.read_text()

def test_cli_validate():
    result=subprocess.run([sys.executable,'-m','skillpack','validate'], cwd=ROOT, text=True, capture_output=True)
    assert result.returncode==0, result.stdout + result.stderr
