import torch
from torch import nn


class CNNEmbedding(nn.Module):
	
	def __init__(self, embed_dim: int, seq_length: int = 16, kernel_sizes=(2, 3, 4), activation=nn.ReLU(inplace=True),
	             embedding=None, num_embeddings: int = None):
		super().__init__()
		if embedding is None:
			assert num_embeddings, 'num_embeddings must be ge 0'
			self.embedding = nn.Embedding(num_embeddings, embed_dim)
		elif isinstance(embedding, nn.Embedding):
			self.embedding = embedding
		elif isinstance(embedding, torch.Tensor):
			self.embedding = nn.Embedding.from_pretrained(embedding)
		else:
			self.embedding = nn.Embedding.from_pretrained(torch.tensor(embedding, dtype=torch.float))
		
		self.convs = nn.ModuleList([
			nn.Sequential(
				nn.Conv1d(in_channels=embed_dim, out_channels=embed_dim, kernel_size=kernel_size, bias=False),
				activation,  # inplace为True，将会改变输入的数据 ，否则不会改变原输入，只会产生新的输出
				nn.AdaptiveMaxPool1d(seq_length)
			) for kernel_size in kernel_sizes
		])
	
	def forward(self, input_ids):
		embeddings = self.embedding(input_ids)
		embeddings = embeddings.transpose(2, 1)
		output = torch.cat([conv(embeddings) for conv in self.convs], dim=-1)
		return output.transpose(2, 1)
	