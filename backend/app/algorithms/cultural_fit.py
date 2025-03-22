from ..models import Program

def assess_cultural_compatibility(user, preferences):
    all_programs = Program.objects.all()
    scored_programs = []

    for program in all_programs:
        score = 0

        if preferences.preferred_language and preferences.preferred_language.lower() in program.languages_offered.lower():
            score += 30

        if preferences.preferred_climate and preferences.preferred_climate.lower() in program.location_climate.lower():
            score += 20

        if preferences.social_environment and preferences.social_environment.lower() in program.campus_life.lower():
            score += 20

        if preferences.prefers_large_city == program.is_in_large_city:
            score += 15

        if preferences.prefers_student_community and program.has_large_international_student_body:
            score += 15

        if score > 0:
            scored_programs.append({"program": program, "score": score})

    return sorted(scored_programs, key=lambda x: x["score"], reverse=True)