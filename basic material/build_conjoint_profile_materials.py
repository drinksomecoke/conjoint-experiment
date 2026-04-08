from __future__ import annotations

import csv
import json
from pathlib import Path


OUT_DIR = Path("/Users/dingshaokai/work/cv_project/conjoint experiment/basic material")


AI_CONTEXTS = [
    ("customer feedback review", "customer feedback comments", "weekly reporting summaries"),
    ("sales reporting", "monthly sales records", "summary dashboards for managers"),
    ("inventory tracking", "inventory reconciliation tasks", "stock exception summaries"),
    ("marketing analysis", "campaign performance notes", "recurring campaign reports"),
    ("recruiting support", "candidate screening notes", "interview scheduling updates"),
    ("budget reconciliation", "expense entries from multiple teams", "monthly budget summaries"),
    ("operations reporting", "service request logs", "operations status updates"),
    ("survey analysis", "survey response files", "summary tables for presentations"),
    ("vendor coordination", "vendor comparison notes", "procurement status summaries"),
    ("appointment scheduling", "client scheduling requests", "calendar coordination updates"),
    ("billing review", "billing exception records", "payment follow-up summaries"),
    ("quality tracking", "quality review comments", "issue tracking summaries"),
    ("training support", "training feedback forms", "session recap notes"),
    ("document review", "repetitive document comparison tasks", "version control checklists"),
    ("social media reporting", "engagement data exports", "weekly content performance summaries"),
    ("market research", "competitor pricing notes", "comparison tables for staff meetings"),
    ("logistics coordination", "shipment status updates", "daily fulfillment summaries"),
    ("client onboarding", "new client intake forms", "onboarding status trackers"),
    ("event planning", "registration and attendance records", "post-event recap summaries"),
    ("compliance support", "policy review checklists", "compliance tracking summaries"),
]


COURSEWORK_TOPICS = [
    "Introductory Machine Learning",
    "Applied Artificial Intelligence",
    "Data Mining and Predictive Analytics",
    "Statistical Learning Methods",
    "AI for Business Decision-Making",
    "Machine Learning for Social Data",
    "Computational Modeling and AI",
    "Supervised Learning Applications",
    "AI Tools for Information Systems",
    "Foundations of Machine Learning",
    "Practical AI in Organizations",
    "Machine Learning for Forecasting",
    "Decision Analytics with AI Methods",
    "Applied Natural Language Processing",
    "Intro to Intelligent Systems",
    "AI and Data-Driven Problem Solving",
    "Machine Learning in Practice",
    "Business Analytics with AI Tools",
    "Predictive Modeling and AI",
    "AI Applications for Operations",
]


INTERNSHIP_CONTEXTS = [
    ("data reporting", "Data Operations Intern", "Business Analyst Intern"),
    ("client support", "Operations Intern", "Client Strategy Intern"),
    ("marketing analytics", "Marketing Intern", "Marketing Analytics Intern"),
    ("financial reporting", "Finance Intern", "Financial Planning Intern"),
    ("supply chain coordination", "Operations Intern", "Supply Chain Analyst Intern"),
    ("research support", "Research Assistant Intern", "Market Research Intern"),
    ("people operations", "HR Intern", "People Analytics Intern"),
    ("sales support", "Sales Operations Intern", "Commercial Strategy Intern"),
    ("customer success", "Customer Success Intern", "Customer Insights Intern"),
    ("project coordination", "Project Support Intern", "Project Management Intern"),
    ("healthcare administration", "Administrative Intern", "Healthcare Operations Intern"),
    ("nonprofit program support", "Program Intern", "Program Analytics Intern"),
    ("retail planning", "Merchandising Intern", "Retail Strategy Intern"),
    ("insurance support", "Claims Intern", "Business Process Intern"),
    ("education services", "Program Assistant Intern", "Education Operations Intern"),
    ("real estate support", "Leasing Intern", "Real Estate Analyst Intern"),
    ("hospitality operations", "Hospitality Intern", "Revenue Operations Intern"),
    ("product support", "Product Operations Intern", "Product Analyst Intern"),
    ("communications support", "Communications Intern", "Corporate Communications Intern"),
    ("procurement support", "Procurement Intern", "Procurement Analyst Intern"),
]


NO_INTERNSHIP_VARIANTS = [
    ("Library Student Assistant", "campus library circulation desk", "helped maintain records and answered routine student questions"),
    ("Admissions Ambassador", "university admissions office", "supported campus visit logistics and responded to prospective student questions"),
    ("Peer Tutor", "academic support center", "provided weekly tutoring sessions and tracked attendance"),
    ("Residence Hall Assistant", "student housing office", "coordinated resident check-ins and documented maintenance requests"),
    ("Student Event Assistant", "campus events office", "organized registration materials and supported event setup"),
    ("Bookstore Associate", "campus bookstore", "handled point-of-sale transactions and restocked merchandise"),
    ("Front Desk Assistant", "student recreation center", "managed sign-ins and responded to member inquiries"),
    ("Office Assistant", "department administrative office", "scheduled appointments and maintained filing systems"),
    ("Community Volunteer Coordinator", "student service club", "organized volunteer sign-ups and tracked participation"),
    ("Orientation Leader", "new student orientation program", "guided incoming students and handled logistics"),
    ("Teaching Assistant", "introductory undergraduate course", "supported grading and held review sessions"),
    ("Dining Services Team Member", "campus dining hall", "handled customer service and shift coordination tasks"),
    ("Campus Technology Helper", "student IT help desk", "resolved basic account and device issues"),
    ("Research Lab Assistant", "faculty lab office", "organized study materials and maintained participant schedules"),
    ("Student Call Center Representative", "alumni relations office", "updated contact records and logged outreach results"),
    ("Fitness Desk Assistant", "university fitness center", "processed check-ins and maintained equipment logs"),
    ("Museum Visitor Assistant", "local museum front desk", "provided visitor support and tracked daily attendance"),
    ("Community Center Assistant", "municipal community center", "coordinated room bookings and responded to inquiries"),
    ("School Program Volunteer", "after-school enrichment program", "supervised activities and recorded attendance"),
    ("Retail Sales Associate", "local retail store", "assisted customers and maintained inventory displays"),
]


SMALL_FIRMS = [
    "North Harbor Insights",
    "Blue Ridge Advisory",
    "Cedar Point Analytics",
    "Maple Street Consulting",
    "Brightwell Strategy Group",
    "Pinecrest Research",
    "Silver Oak Solutions",
    "Redwood Business Services",
    "HarborLine Operations",
    "Summit Trail Partners",
    "Westfield Data Services",
    "Elm Street Advisory",
    "Clearview Market Research",
    "Granite Point Consulting",
    "Northgate Planning",
    "Beacon Hill Analytics",
    "Lakefront Strategy",
    "Oakview Operations",
    "Cornerstone Advisory",
    "Riverbend Insights",
]


WELL_KNOWN_FIRMS = [
    "Deloitte",
    "Amazon",
    "JPMorgan Chase",
    "Accenture",
    "Microsoft",
    "PwC",
    "Bank of America",
    "Target",
    "UnitedHealth Group",
    "IBM",
    "Citi",
    "PepsiCo",
    "Capital One",
    "KPMG",
    "Adobe",
    "Pfizer",
    "American Express",
    "Nike",
    "Comcast",
    "Visa",
]


PROJECT_TOPICS = [
    ("student retention dashboard", "student retention patterns", "interactive dashboard for program staff"),
    ("retail sales analysis", "store-level sales trends", "reporting toolkit for weekly reviews"),
    ("event attendance tracker", "event registration and turnout data", "planning dashboard for organizers"),
    ("budget variance review", "department spending patterns", "summary report for monthly meetings"),
    ("customer service log analysis", "support ticket patterns", "issue categorization dashboard"),
    ("housing demand study", "housing application trends", "forecast summary for planning staff"),
    ("survey insights report", "survey response patterns", "presentation-ready findings for stakeholders"),
    ("inventory reorder tracker", "reorder timing and stock gaps", "tracking sheet for operations staff"),
    ("volunteer scheduling tool", "volunteer shift coverage", "coordination tracker for supervisors"),
    ("billing error review", "common billing exceptions", "checklist for process improvement"),
    ("website traffic summary", "traffic and engagement patterns", "performance dashboard for communications staff"),
    ("course enrollment review", "course enrollment changes", "report for advising staff"),
    ("vendor comparison model", "vendor pricing and service records", "comparison worksheet for procurement review"),
    ("fundraising performance report", "donor campaign results", "summary deck for outreach planning"),
    ("clinic scheduling analysis", "appointment scheduling delays", "tracking dashboard for administrators"),
    ("shipping delay review", "fulfillment timing issues", "operations summary for team leads"),
    ("claims processing review", "claims turnaround times", "workflow summary for supervisors"),
    ("recruitment funnel summary", "applicant funnel stages", "dashboard for recruiting staff"),
    ("membership renewal analysis", "renewal and churn patterns", "report for account managers"),
    ("training attendance tracker", "training completion records", "status dashboard for coordinators"),
]


def build_ai_materials() -> dict:
    labels = {
        "no_ai_related_experience": "No AI-related experience mentioned",
        "gen_ai_workflow_efficiency": "Used generative AI in a project to improve workflow efficiency",
        "independent_ai_automation_project": "Independently completed an AI automation project",
        "ai_ml_coursework": "Completed coursework in AI / machine learning",
    }

    groups = {k: {"label": v, "items": []} for k, v in labels.items()}

    for idx, (context, input_desc, output_desc) in enumerate(AI_CONTEXTS, start=1):
        shared = {
            "id": f"ai_{idx:02d}",
            "context": context,
        }

        groups["no_ai_related_experience"]["items"].append(
            {
                **shared,
                "title": f"{context.title()} Project",
                "summary": f"Completed a project focused on {context} using standard spreadsheet and reporting tools.",
                "bullets": [
                    f"Reviewed {input_desc} and organized findings into {output_desc}.",
                    "Built a consistent process for checking outputs and sharing updates with team members.",
                ],
            }
        )

        groups["gen_ai_workflow_efficiency"]["items"].append(
            {
                **shared,
                "title": f"{context.title()} Project",
                "summary": f"Used generative AI to streamline drafting and review steps in a {context} project.",
                "bullets": [
                    f"Used generative AI to speed up first-pass review of {input_desc} before final manual checks.",
                    f"Reduced repetitive drafting time and delivered {output_desc} more efficiently.",
                ],
            }
        )

        groups["independent_ai_automation_project"]["items"].append(
            {
                **shared,
                "title": f"Independent {context.title()} Automation Project",
                "summary": f"Designed an independent automation workflow to support {context} tasks.",
                "bullets": [
                    f"Built a small automation workflow that standardized {input_desc} and routed outputs into {output_desc}.",
                    "Tested the workflow on sample files, documented exceptions, and refined prompts and logic independently.",
                ],
            }
        )

        topic = COURSEWORK_TOPICS[idx - 1]
        groups["ai_ml_coursework"]["items"].append(
            {
                **shared,
                "title": topic,
                "summary": f"Completed formal coursework covering AI methods with an applied assignment related to {context}.",
                "bullets": [
                    f"Completed assignments on core AI or machine learning concepts and discussed applications to {context}.",
                    "Submitted a course project explaining model selection, evaluation, and practical use considerations.",
                ],
            }
        )

    return {"attribute": "AI-related experience", "groups": groups}


def build_internship_materials() -> dict:
    labels = {
        "no_relevant_internship_experience": "No relevant internship experience",
        "relevant_internship_smaller_firm": "Relevant internship at a smaller firm",
        "relevant_internship_well_known_firm": "Relevant internship at a well-known firm",
    }
    groups = {k: {"label": v, "items": []} for k, v in labels.items()}

    for idx, ((focus, small_role, large_role), no_intern, small_firm, large_firm) in enumerate(
        zip(INTERNSHIP_CONTEXTS, NO_INTERNSHIP_VARIANTS, SMALL_FIRMS, WELL_KNOWN_FIRMS), start=1
    ):
        no_title, no_org, no_desc = no_intern
        groups["no_relevant_internship_experience"]["items"].append(
            {
                "id": f"intern_{idx:02d}",
                "focus_area": focus,
                "title": no_title,
                "organization": no_org,
                "summary": "Held a student or campus role, but no directly relevant internship was listed.",
                "bullets": [
                    no_desc.capitalize() + ".",
                    "Managed recurring responsibilities while balancing coursework and weekly deadlines.",
                ],
            }
        )

        groups["relevant_internship_smaller_firm"]["items"].append(
            {
                "id": f"intern_{idx:02d}",
                "focus_area": focus,
                "title": small_role,
                "organization": small_firm,
                "summary": f"Completed a relevant internship focused on {focus} at a smaller firm.",
                "bullets": [
                    f"Supported day-to-day work related to {focus} and prepared materials for internal team review.",
                    "Worked closely with a small team and handled tasks spanning analysis, coordination, and follow-up.",
                ],
            }
        )

        groups["relevant_internship_well_known_firm"]["items"].append(
            {
                "id": f"intern_{idx:02d}",
                "focus_area": focus,
                "title": large_role,
                "organization": large_firm,
                "summary": f"Completed a relevant internship focused on {focus} at a well-known firm.",
                "bullets": [
                    f"Contributed to projects related to {focus} and supported structured reporting for broader teams.",
                    "Worked within established processes, communicated updates clearly, and delivered materials on schedule.",
                ],
            }
        )

    return {"attribute": "Internship experience", "groups": groups}


def build_project_style_materials() -> dict:
    labels = {
        "without_quantified_results": "Project experience described without quantified results",
        "with_quantified_results": "Project experience includes quantified results",
    }
    groups = {k: {"label": v, "items": []} for k, v in labels.items()}

    metrics = [
        "cut preparation time by 18%",
        "improved reporting turnaround by 22%",
        "reduced manual review effort by 15%",
        "increased data accuracy by 12%",
        "shortened update cycles by 20%",
        "improved completion rates by 14%",
        "reduced follow-up delays by 19%",
        "improved response tracking by 17%",
        "reduced stockout exceptions by 13%",
        "improved scheduling visibility by 21%",
        "lowered billing review time by 16%",
        "improved content reporting speed by 23%",
        "reduced advising prep time by 18%",
        "improved vendor comparison turnaround by 20%",
        "raised campaign follow-up efficiency by 15%",
        "cut scheduling backlog by 17%",
        "reduced delay review time by 14%",
        "improved funnel reporting speed by 19%",
        "increased renewal tracking accuracy by 11%",
        "raised training status visibility by 24%",
    ]

    for idx, ((name, subject, output), metric) in enumerate(zip(PROJECT_TOPICS, metrics), start=1):
        groups["without_quantified_results"]["items"].append(
            {
                "id": f"project_{idx:02d}",
                "project_name": name.title(),
                "summary": f"Developed a project analyzing {subject} and presented findings in an {output}.",
                "bullets": [
                    f"Collected and cleaned data related to {subject}.",
                    f"Built an {output} and shared recommendations with stakeholders.",
                ],
            }
        )
        groups["with_quantified_results"]["items"].append(
            {
                "id": f"project_{idx:02d}",
                "project_name": name.title(),
                "summary": f"Developed a project analyzing {subject} and presented findings in an {output}.",
                "bullets": [
                    f"Collected and cleaned data related to {subject}.",
                    f"Built an {output} that {metric}.",
                ],
            }
        )

    return {"attribute": "Project achievement style", "groups": groups}


def write_materials(filename_stem: str, payload: dict) -> list[dict]:
    json_path = OUT_DIR / f"{filename_stem}.json"
    csv_path = OUT_DIR / f"{filename_stem}.csv"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rows: list[dict] = []
    for group_key, group in payload["groups"].items():
        for item in group["items"]:
            rows.append(
                {
                    "attribute": payload["attribute"],
                    "level_key": group_key,
                    "level_label": group["label"],
                    **{k: v for k, v in item.items() if k != "bullets"},
                    "bullet_1": item["bullets"][0],
                    "bullet_2": item["bullets"][1],
                }
            )

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ai_rows = write_materials("ai_related_experience_materials", build_ai_materials())
    internship_rows = write_materials("internship_experience_materials", build_internship_materials())
    project_rows = write_materials("project_achievement_style_materials", build_project_style_materials())

    combined = ai_rows + internship_rows + project_rows
    combined_json = OUT_DIR / "conjoint_profile_materials_combined.json"
    combined_csv = OUT_DIR / "conjoint_profile_materials_combined.csv"
    combined_json.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fieldnames: list[str] = []
    for row in combined:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with combined_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(combined)


if __name__ == "__main__":
    main()
