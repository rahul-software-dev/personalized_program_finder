from ..models import Program

def match_teaching_style(user, preferences):
    all_programs = Program.objects.all()
    scored_programs = []

    for program in all_programs:
        score = 0

        if preferences.prefers_practical_learning and program.is_project_based:
            score += 30

        if preferences.prefers_research_focus and program.has_research_intensive_courses:
            score += 25

        if preferences.prefers_interactive_classes and program.has_small_class_sizes:
            score += 20

        if preferences.prefers_self_paced and program.supports_self_paced_learning:
            score += 15

        if preferences.prefers_traditional_lectures and program.is_theory_focused:
            score += 10

        if score > 0:
            scored_programs.append({"program": program, "score": score})

    return sorted(scored_programs, key=lambda x: x["score"], reverse=True)