
import os
from dataclasses import dataclass
from langchain.tools.tavily_search import TavilySearchResults
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.language_models.llms import LLM
from langgraph.graph import StateGraph
import google.generativeai as genai

os.environ['TAVILY_API_KEY'] = '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'
os.environ['GOOGLE_API_KEY'] = 'AIzaSyBS7fzCawaHqWTZcCm4IKOnxz72DrahpJg'

tavily_tool = TavilySearchResults(k=5)

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def google_generate(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')  # or 'models/text-bison-001' for PaLM
    response = model.generate_content(prompt)
    return response.text

class GoogleLLM(LLM):
    def _call(self, prompt, stop=None):
        return google_generate(prompt)

    @property
    def _llm_type(self):
        return "google"

google_llm = GoogleLLM()

research_prompt = PromptTemplate.from_template(
    "Summarize the following search results into key points:\n{search_results}"
)
draft_prompt = PromptTemplate.from_template(
    "Based on the research points below, write a detailed and structured answer:\n{research_summary}"
)

research_chain = LLMChain(llm=google_llm, prompt=research_prompt)
draft_chain = LLMChain(llm=google_llm, prompt=draft_prompt)

@dataclass
class ResearchState:
    query: str = None
    search_results: str = None
    research_summary: str = None
    drafted_answer: str = None

graph = StateGraph(ResearchState)

def search_web(state: ResearchState):
    query = state.query
    results = tavily_tool.run(query)
    return {"search_results": str(results)}

def summarize_results(state: ResearchState):
    summary = research_chain.run(search_results=state.search_results)
    return {"research_summary": summary}

def draft_answer(state: ResearchState):
    answer = draft_chain.run(research_summary=state.research_summary)
    return {"drafted_answer": answer}

graph.add_node("search_web", search_web)
graph.add_node("summarize_results", summarize_results)
graph.add_node("draft_answer", draft_answer)

graph.set_entry_point("search_web")
graph.add_edge("search_web", "summarize_results")
graph.add_edge("summarize_results", "draft_answer")
graph.set_finish_point("draft_answer")

compiled_graph = graph.compile()

if __name__ == "__main__":
    user_query = input("Enter your research question: ")

    initial_state = ResearchState(query=user_query)

    result = compiled_graph.invoke(initial_state)

    print("\n" + "="*50)
    print("--- Final Drafted Answer ---\n")
    print(result['drafted_answer'])
    print("="*50 + "\n")

