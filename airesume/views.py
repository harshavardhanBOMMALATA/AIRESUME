from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

groq_api_key="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"

import re
from openai import OpenAI


@csrf_exempt
def education_api(request):
    try:
        body = json.loads(request.body)
        education_data = body.get("data", "no_mentionings_properly")
        job_title = body.get("job_title", "no_mentionings_properly")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Give exactly 5 evaluation points.
Each point maximum 5 words.
Mix strengths and weaknesses for the job title: {job_title}.
Number them 1 to 5.

Education: {education_data}
this is for education only, ignore other sections.
mostly focus on the latest education, but also consider the previous ones.
at last give overall score out of 100 for education section in 6th point.
6.score.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content

        print("===== AI FULL RESPONSE =====")
        print(result_text)
        lines = result_text.splitlines()
        digit=""
        for i in lines[-1][1:]:
            if i.isdigit():
                digit+=i
            if i=='/':
                break
        if digit=="":
            digit="0"
        print("============================")

        return JsonResponse({"result": lines[:-1], "score": digit})

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)




@csrf_exempt
def skills_api(request):
    try:
        body = json.loads(request.body)
        skills_data = body.get("data", "no_mentionings_properly")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Give exactly 5 evaluation points.
Each point maximum 5 words.
Mix strengths and weaknesses for the job title: {body.get("job_title", "no_mentionings_properly")}.
Number them 1 to 5.

Skills: {skills_data}
this is for skills only, ignore other sections.
mostly focus on the skills for {body.get("job_title", "no_mentionings_properly")}, but also consider extra also.
at last give overall score out of 100 for skills section in 6th point.
6.score.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content

        print("===== AI FULL RESPONSE =====")
        print(result_text)
        lines = result_text.splitlines()
        digit=""
        for i in lines[-1][1:]:
            if i.isdigit():
                digit+=i
            if i=='/':
                break
        if digit=="":
            digit="0"
        print("============================")

        return JsonResponse({"result": lines[:-1], "score": digit})

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)










@csrf_exempt
def projects_api(request):
    try:
        body = json.loads(request.body)
        projects_data = body.get("data", "no_mentionings_properly")
        job_title = body.get("job_title", "no_mentionings_properly")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Give exactly 5 evaluation points.
Each point maximum 5 words.
Mix strengths and weaknesses for the job title: {job_title}.
Number them 1 to 5.

Projects: {projects_data}
this is for projects only, ignore other sections.
mostly focus on project relevance to {job_title}.
at last give overall score out of 100 for projects section in 6th point.
6.score.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content

        print("===== AI FULL RESPONSE =====")
        print(result_text)

        lines = result_text.splitlines()

        digit = ""
        for i in lines[-1][1:]:
            if i.isdigit():
                digit += i
            if i == '/':
                break

        if digit == "":
            digit = "0"

        print("============================")

        return JsonResponse({
            "result": lines[:-1],
            "score": digit
        })

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)




@csrf_exempt
def certifications_api(request):
    try:
        body = json.loads(request.body)
        certifications_data = body.get("data", "no_mentionings_properly")
        job_title = body.get("job_title", "no_mentionings_properly")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Give exactly 5 evaluation points.
Each point maximum 5 words.
Mix strengths and weaknesses for the job title: {job_title}.
Number them 1 to 5.

Certifications: {certifications_data}
this is for certifications only, ignore other sections.
mostly focus on certification relevance to {job_title}.
at last give overall score out of 100 for certifications section in 6th point.
6.score.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content

        print("===== AI FULL RESPONSE =====")
        print(result_text)

        lines = result_text.splitlines()

        digit = ""
        for i in lines[-1][1:]:
            if i.isdigit():
                digit += i
            if i == '/':
                break

        if digit == "":
            digit = "0"

        print("============================")

        return JsonResponse({
            "result": lines[:-1],
            "score": digit
        })

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)





@csrf_exempt
def achievements_api(request):
    try:
        body = json.loads(request.body)
        achievements_data = body.get("data", "no_mentionings_properly")
        job_title = body.get("job_title", "no_mentionings_properly")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Give exactly 5 evaluation points.
Each point maximum 5 words.
Mix strengths and weaknesses for the job title: {job_title}.
Number them 1 to 5.

Achievements: {achievements_data}
this is for achievements only, ignore other sections.
mostly focus on achievement relevance to {job_title}.
at last give overall score out of 100 for achievements section in 6th point.
6.score.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content

        print("===== AI FULL RESPONSE =====")
        print(result_text)

        lines = result_text.splitlines()

        digit = ""
        for i in lines[-1][1:]:
            if i.isdigit():
                digit += i
            if i == '/':
                break

        if digit == "":
            digit = "0"

        print("============================")

        return JsonResponse({
            "result": lines[:-1],
            "score": digit
        })

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)



@csrf_exempt
def experience_api(request):
    try:
        body = json.loads(request.body)
        experience_data = body.get("data", "no_mentionings_properly")
        job_title = body.get("job_title", "no_mentionings_properly")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Give exactly 5 evaluation points.
Each point maximum 5 words.
Mix strengths and weaknesses for the job title: {job_title}.
Number them 1 to 5.

Experience: {experience_data}
this is for experience only, ignore other sections.
mostly focus on experience relevance to {job_title}.
at last give overall score out of 100 for experience section in 6th point.
6.score.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content

        print("===== AI FULL RESPONSE =====")
        print(result_text)

        lines = result_text.splitlines()

        digit = ""
        for i in lines[-1][1:]:
            if i.isdigit():
                digit += i
            if i == '/':
                break

        if digit == "":
            digit = "0"

        print("============================")

        return JsonResponse({
            "result": lines[:-1],
            "score": digit
        })

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)




@csrf_exempt
def others_api(request):
    try:
        body = json.loads(request.body)
        others_data = body.get("data", "no_mentionings_properly")
        job_title = body.get("job_title", "no_mentionings_properly")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Give exactly 5 evaluation points.
Each point maximum 5 words.
Mix strengths and weaknesses for the job title: {job_title}.
Number them 1 to 5.

Other Information: {others_data}
this is for other information only, ignore other sections.
focus on relevance to {job_title}.
at last give overall score out of 100 for this section in 6th point.
6.score.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content

        print("===== AI FULL RESPONSE =====")
        print(result_text)

        lines = result_text.splitlines()

        digit = ""
        for i in lines[-1][1:]:
            if i.isdigit():
                digit += i
            if i == '/':
                break

        if digit == "":
            digit = "0"

        print("============================")

        return JsonResponse({
            "result": lines[:-1],
            "score": digit
        })

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)




@csrf_exempt
def overall_summary_api(request):
    try:
        body = json.loads(request.body)
        resume_data = body.get("data", "no_mentionings_properly")
        job_title = body.get("job_title", "no_mentionings_properly")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Give exactly 5 overall evaluation points.
Each point maximum 6 words.
Mix strengths and weaknesses for the job title: {job_title}.
Number them 1 to 5.

This is the full resume content:
{resume_data}

Evaluate overall profile strength, relevance, clarity, and impact.
At last give overall resume score out of 100 in 6th point.
6.score.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content

        print("===== AI FULL RESPONSE =====")
        print(result_text)

        lines = result_text.splitlines()

        digit = ""
        for i in lines[-1][1:]:
            if i.isdigit():
                digit += i
            if i == '/':
                break

        if digit == "":
            digit = "0"

        print("============================")

        return JsonResponse({
            "result": lines[:-1],
            "score": digit
        })

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)




@csrf_exempt
def overall_resume_score_api(request):
    try:
        body = json.loads(request.body)
        resume_data = body.get("data", "no_mentionings_properly")
        job_title = body.get("job_title", "Software Engineer")

        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        prompt = f"""
Evaluate the following resume for the job role: {job_title}.

Give only one overall score out of 100 based on relevance, skills match, experience, education, and projects.

Return strictly in this format:
Score: XX/100

Resume:
{resume_data}
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        result_text = response.choices[0].message.content.strip()

        print("===== AI RESPONSE =====")
        print(result_text)

        # Extract only first number before '/'
        score = 0
        if "/" in result_text:
            score_part = result_text.split("/")[0]
            digits = "".join(ch for ch in score_part if ch.isdigit())
            score = digits if digits else "0"
        else:
            digits = "".join(ch for ch in result_text if ch.isdigit())
            score = digits if digits else "0"

        print("========================")

        return JsonResponse({"score": score})

    except Exception as e:
        print("Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)
