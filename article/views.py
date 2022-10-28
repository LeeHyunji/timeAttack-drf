from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        all_articles = Article.objects.all()
        return Response(ArticleSerializer(all_articles, many=True).data)
        
    def post(self, request):
        article = ArticleSerializer(data=request.data)
        article.is_valid(raise_exception=True) # 검증 단계에서 문제가 있을 경우 에러 발생
        article.save() # 검증 단계에서 문제가 없을 경우 데이터 저장
        
        return Response(article.data)
