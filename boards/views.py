from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed
from .models import Board
from .forms import BoardForm

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    content = { 'boards':boards, }
    return render(request, 'boards/index.html', content)

def create(request):
    
    if request.method == 'POST':
        # Binding: form 인스턴스를 생성하고 요청(request.POST)로 데이터를 채운다.
        form = BoardForm(request.POST)
        
        # form 유효성 체크
        if form.is_valid():
            # cleaned_data 는 QueryDict 를 return 하기 때문에 .get을 사용가능
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # 검증을 통과한 깨끗한 데이터를 가져와서 board 인스턴스 생성 및 추가
            # board = Board.objects.create(title=title, content=content)

            # ModelForm을 적용 이후
            board = form.save()
            return redirect('boards:detail', board.pk)
    # GET: 기본 form 인스턴스를 생성
    else:
        form = BoardForm()
    # GET: 기본 form 의 모습
    # POST: 요청에서 검증에 실패한 form 이며 오류메시지를 포함한 상태임
    context = {'form':form}
    return render(request, 'boards/form.html', context)

def detail(request, board_pk):
    # board = Board.objects.get(pk=board_pk)
    board = get_object_or_404(Board, pk=board_pk)   # 없는 페이지로 접근 시 에러메시지 표시
    content = { 'board':board, }
    return render(request, 'boards/detail.html', content)


def update(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save()
            # board.title = form.cleaned_data.get('title')
            # board.content = form.cleaned_data.get('content')
            # board.save()

            return redirect('boards:detail', board.pk)
        
    else:
        # form = BoardForm(initial=board.__dict__)
        form = BoardForm(instance=board)
        

    context={ 'form':form,
              'board':board,  
             }
    return render(request, 'boards/form.html', context)


def delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        board.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:detail', board.pk)