# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    content = doc_dict.get("content", "")
    
    if not content or len(content) < 10:
        return False
    
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    for kw in toxic_keywords:
        if kw in content:
            return False
            
    return True
