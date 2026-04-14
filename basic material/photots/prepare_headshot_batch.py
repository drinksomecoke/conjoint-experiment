from __future__ import annotations

import json
from pathlib import Path


BASE_PROMPT = (
    "Create a photorealistic studio headshot for a hiring experiment. "
    "The subject should look average-looking and ordinary, not especially attractive "
    "and not especially unattractive. Keep expression neutral with a faint closed-mouth "
    "smile. Use a direct front-facing pose, centered head-and-shoulders framing, plain "
    "light gray background, soft even studio lighting, natural skin texture, no dramatic "
    "shadows, no beauty retouching, no glamour styling, no heavy makeup, no facial hair "
    "beyond normal subtle grooming if applicable, no glasses, no jewelry, no hats, no "
    "visible logos, no watermark. Clothing should be a simple medium-gray crew-neck t-shirt. "
    "Age should appear approximately 25 to 38. Keep camera angle, crop, lighting, clothing, "
    "background, expression intensity, and overall attractiveness level highly consistent "
    "across all categories. Within each race-gender group, make the ten people clearly "
    "different from one another while keeping all of them ordinary and comparable in "
    "attractiveness."
)


CATEGORIES = [
    ("black", "male", "Black adult man"),
    ("black", "female", "Black adult woman"),
    ("white", "male", "White adult man"),
    ("white", "female", "White adult woman"),
    ("latino", "male", "Latino adult man"),
    ("latino", "female", "Latina adult woman"),
    ("asian_chinese", "male", "Chinese adult man"),
    ("asian_chinese", "female", "Chinese adult woman"),
]


VARIATIONS = [
    "rounder face, softer jawline, fuller cheeks, short neat hair, medium skin tone for the group",
    "longer oval face, narrower jaw, slightly higher forehead, tidy side-part hairstyle, slightly lighter skin tone for the group",
    "broader face, stronger but not model-like jaw, close-cropped hair, slightly darker skin tone for the group",
    "heart-shaped face, smaller chin, slightly fuller lips, simple natural hairstyle, average skin tone for the group",
    "rectangular face, prominent cheekbones, straight natural hairline, slightly uneven but realistic skin texture",
    "softer facial features, lower cheekbones, wider nose bridge, neat low-maintenance hairstyle",
    "slimmer face, longer nose, subtle under-eye texture, simple professional grooming",
    "wider face, shorter forehead, fuller jaw area, natural hair volume without styling",
    "angular face, defined brow area, modest asymmetry, plain everyday hairstyle",
    "balanced oval face, distinct nose and mouth shape from the other variants, natural complexion variation",
]


def build_job(race: str, gender: str, subject: str, index: int) -> dict:
    variation = (
        f"Variant {index}: {VARIATIONS[index - 1]}. "
        "Make this individual visibly distinct from the other variants in the same "
        "race-gender group, but do not make them unusually attractive, unattractive, "
        "stylized, expressive, or memorable for non-face reasons."
    )
    return {
        "prompt": f"{BASE_PROMPT} {variation}",
        "use_case": "photorealistic-natural",
        "scene": "passport-style studio portrait with a plain light gray backdrop",
        "subject": subject,
        "style": "photorealistic professional ID-style headshot",
        "composition": "front-facing, centered, symmetrical head-and-shoulders portrait, camera at eye level",
        "lighting": "soft even studio lighting, neutral mood, no dramatic contrast",
        "constraints": (
            "average-looking face; consistent attractiveness level across all images; "
            "same shirt color and background; no accessories; no text; no watermark"
        ),
        "negative": (
            "glamour photography, strong smile, extreme attractiveness, extreme unattractiveness, "
            "fashion styling, colored background, dramatic lighting, side profile"
        ),
        "size": "1024x1024",
        "quality": "medium",
        "out": f"{race}_{gender}_{index:02d}.png",
    }


def main() -> None:
    root = Path("/Users/dingshaokai/work/cv_project")
    out_dir = root / "tmp" / "imagegen"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "controlled_headshots.jsonl"

    jobs = []
    for race, gender, subject in CATEGORIES:
        for idx in range(1, 11):
            jobs.append(build_job(race, gender, subject, idx))

    with out_path.open("w", encoding="utf-8") as f:
        for job in jobs:
            f.write(json.dumps(job, ensure_ascii=False) + "\n")

    print(out_path)
    print(f"jobs={len(jobs)}")


if __name__ == "__main__":
    main()
