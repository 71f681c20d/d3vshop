# DevShop Design

Operating model for the dev shop

- Waterfall development model
    - Agile development doesn't make sense since AI can do waterfalls quickly, so preserves fast release cycles

DevShop patterns
- Where should sequential chats be nested?
    - Each step in the waterfall is a sequential chat between a worker and a critic
    - After the critic approves of the completed task, the completed task can be bubbled up to another critic for a final approval
    - Having multiple layers of approval should allow the nested critic to maintain development details in-context for providing feedback
    - The parent critic can then perform final approval without packing the context window with unnecessary details, allowing it to be more objective, predictable, and unchanging. This will help to consistently produce quality results.

What about group chats?
- When should group chats be used?
    - In situations where 
- When should nested group chats be used?
- When should group chats be nested into sequential chats?


