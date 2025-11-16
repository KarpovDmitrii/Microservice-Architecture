from fastapi import APIRouter, Depends
from src.schemas.CommentSchemas import CreateCommentSchema, CommentResponseSchema
from src.controllers.AuthorizationController import access_token_required
from src.models.Database import get_db
from src.controllers import CommentController
from typing import List

CommentRouter = APIRouter()

@CommentRouter.post("/articles/{article_id}/comments", tags=["comments"])
async def add_comment(id: str, comment: CreateCommentSchema,
                      token_data = Depends(access_token_required),
                      db = Depends(get_db)):
    answer = await CommentController.add_comment(comment, id, token_data, db)
    return answer


@CommentRouter.get("/articles/{article_id}/comments", tags=["comments"])
async def get_comments(id: str, db = Depends(get_db)):
    answer = await CommentController.get_comments(id, db)
    return answer


@CommentRouter.delete("/articles/{article_id}/comments/{comment_id}", tags=["comments"])
async def delete_comment(article_id: str, comment_id: str, token_data = Depends(access_token_required), db = Depends(get_db)):
    answer = await CommentController.delete_comment(article_id, comment_id, token_data, db)
    return answer
