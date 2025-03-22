from ..models import Program

def align_programs_with_career_goals(user, preferences):
    """
    Aligns programs with a user's career goals and returns a ranked list.

    Args:
        user (User): The user object requesting recommendations.
        preferences (UserPreference): The user's stored preferences.

    Returns:
        List[Dict]: A ranked list of programs based on career alignment scores.
    """

    all_programs = Program.objects.all()
    scored_programs = []

    for program in all_programs:
        score = 0

        # Matching by career field relevance
        if preferences.career_goal.lower() in program.career_outcomes.lower():
            score += 35

        # Matching by job placement rate
        if program.job_placement_rate and program.job_placement_rate >= 80:
            score += 20

        # Matching by industry partnerships
        if program.has_industry_partnerships:
            score += 15

        # Matching by internship opportunities
        if preferences.prefers_internships and program.has_internship_opportunities:
            score += 10

        # Matching by alumni success rate
        if program.alumni_success_rate and program.alumni_success_rate >= 75:
            score += 10

        # Matching by specialization in demand
        if preferences.specialization and preferences.specialization.lower() in program.specializations.lower():
            score += 10

        # Storing program with its score
        if score > 0:
            scored_programs.append({"program": program, "score": score})

    # Sort programs by score in descending order
    ranked_programs = sorted(scored_programs, key=lambda x: x["score"], reverse=True)

    return ranked_programs