import argparse, json, pathlib, sys, re
ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_MD_SECTIONS = ["## Purpose", "## When to use this skill", "## Required user inputs", "## Operating workflow", "## Output format", "## Expected outputs", "## Guardrails", "## Production contract"]

def load_index():
    return json.loads((ROOT / "skills-index.json").read_text())

def find_skill(slug):
    for item in load_index():
        if item["slug"] == slug or item["name"].lower() == slug.lower():
            return item
    raise SystemExit(f"Skill not found: {slug}")

def list_skills(args):
    items = load_index()
    for item in items:
        if args.category and item["category"] != args.category:
            continue
        print(f"{item['slug']}\t{item['category']}\t{item['name']}")

def validate(args):
    errors=[]
    for item in load_index():
        p=ROOT / item["path"]
        manifest=ROOT / item.get("manifest", str(p.parent / "skill.json"))
        sample=p.parent / "sample-input.json"
        for f in [p, manifest, sample, p.parent/"README.md", p.parent/"examples.md"]:
            if not f.exists(): errors.append(f"Missing {f.relative_to(ROOT)}")
        if p.exists():
            txt=p.read_text()
            for sec in REQUIRED_MD_SECTIONS:
                if sec not in txt: errors.append(f"{p.relative_to(ROOT)} missing {sec}")
        if manifest.exists():
            try:
                data=json.loads(manifest.read_text())
                for k in ["id","name","slug","version","category","description","inputs","outputs","workflow","guardrails"]:
                    if k not in data: errors.append(f"{manifest.relative_to(ROOT)} missing {k}")
            except Exception as e:
                errors.append(f"Invalid JSON {manifest.relative_to(ROOT)}: {e}")
    if errors:
        print("Validation failed:")
        for e in errors: print("-", e)
        sys.exit(1)
    print("Validation passed. All skills include prompts, manifests, samples, and production contracts.")

def render(args):
    item=find_skill(args.skill)
    skill_md=(ROOT/item["path"]).read_text()
    payload={}
    if args.input:
        payload=json.loads(pathlib.Path(args.input).read_text()) if pathlib.Path(args.input).exists() else json.loads(args.input)
    else:
        sample=json.loads(((ROOT/item["path"]).parent/"sample-input.json").read_text())
        payload=sample
    print("# SYSTEM / SKILL INSTRUCTIONS\n")
    print(skill_md)
    print("\n# USER RUNTIME INPUT\n")
    print(json.dumps(payload, indent=2))

def new_adapter_prompt(args):
    item=find_skill(args.skill)
    print(f"Use the skill at {item['path']}. Follow its production contract. Here is my input:\n\n{args.text or '[paste input here]'}")

def main():
    parser=argparse.ArgumentParser(prog="skillpack", description="Validate and render portable AI skills.")
    sub=parser.add_subparsers(required=True)
    p=sub.add_parser("list"); p.add_argument("--category"); p.set_defaults(func=list_skills)
    p=sub.add_parser("validate"); p.set_defaults(func=validate)
    p=sub.add_parser("render"); p.add_argument("skill"); p.add_argument("--input"); p.set_defaults(func=render)
    p=sub.add_parser("prompt"); p.add_argument("skill"); p.add_argument("--text"); p.set_defaults(func=new_adapter_prompt)
    args=parser.parse_args(); args.func(args)
if __name__ == "__main__": main()
