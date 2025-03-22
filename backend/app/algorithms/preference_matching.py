"""
Algorithm for matching academic programs to user preferences.

This module evaluates user preferences and ranks academic programs based on 
relevance, considering factors like location, field of study, cost, 
research opportunities, and more.
"""

from ..models import Program

def match_programs_based_on_preferences(user, preferences):
    """
    Matches programs to a user's preferences and returns a ranked list.

    Args:
        user (User): The user object requesting recommendations.
        preferences (UserPreference): The user's stored preferences.

    Returns:
        List[Dict]: A ranked list of program recommendations with scores.
    """

    all_programs = Program.objects.all()
    scored_programs = []

    for program in all_programs:
        score = 0

        # Matching by field of study
        if preferences.field_of_study.lower() in program.field_of_study.lower():
            score += 30

        # Matching by preferred country
        if preferences.preferred_country and preferences.preferred_country.lower() == program.country.lower():
            score += 20

        # Matching by tuition fee range
        if preferences.max_tuition_fee and program.tuition_fee <= preferences.max_tuition_fee:
            score += 15

        # Matching by research opportunities
        if preferences.research_opportunities and program.research_opportunities:
            score += 10

        # Matching by teaching methodology preference
        if preferences.teaching_style and preferences.teaching_style.lower() == program.teaching_style.lower():
            score += 10

        # Matching by scholarship availability
        if preferences.requires_scholarship and program.has_scholarship:
            score += 10

        # Matching by language preference
        if preferences.language and preferences.language.lower() == program.language.lower():
            score += 5

        # Storing program with its score
        if score > 0:
            scored_programs.append({"program": program, "score": score})

    # Sort programs by score in descending order
    ranked_programs = sorted(scored_programs, key=lambda x: x["score"], reverse=True)

    return ranked_programs