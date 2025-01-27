from manim import *

class BitcoinExplanation(Scene):
    def construct(self):
        # Section 1: Transactions and Blocks
        title1 = Text("Bitcoin Transactions", font_size=36).to_edge(UP)
        self.play(Write(title1))
        
        # Create participants
        alice = ImageMobject("assets/bitcoin-alice.png").scale(0.5)
        bob = ImageMobject("assets/bitcoin-bob.png").scale(0.5)
        group = Group(alice, bob).arrange(RIGHT, buff=2)
        self.play(FadeIn(group))
        
        # Transaction animation
        arrow = Arrow(alice.get_right(), bob.get_left(), buff=0.2)
        transaction_text = Text("1 BTC", font_size=24).next_to(arrow, UP)
        self.play(
            GrowArrow(arrow),
            Write(transaction_text)
        )
        self.wait(2)

        # Convert transaction to data structure
        transaction_data = VGroup(
            Text("Transaction Data:", font_size=24),
            Text("Sender: Alice", font_size=20, color=BLUE),
            Text("Receiver: Bob", font_size=20, color=GREEN),
            Text("Amount: 1 BTC", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT).shift(DOWN*2)
        self.play(Transform(transaction_text, transaction_data))
        self.wait(2)

        # Section 2: Blockchain
        self.clear_scene()
        title2 = Text("Blockchain Structure", font_size=36).to_edge(UP)
        self.play(Write(title2))

        blocks = VGroup(*[VGroup(
            Rectangle(height=2, width=3, color=WHITE),
            Text(f"Block {i+1}", font_size=24),
            Text(f"Hash: a1b2c3...\nPrev: d4e5f6...", font_size=14)
        ).arrange(DOWN, buff=0.2) for i in range(3)]).arrange(RIGHT, buff=1)
        
        for block in blocks:
            self.play(Create(block[0]), Write(block[1]), Write(block[2]))
            self.wait(0.5)
        
        arrows = VGroup()
        for i in range(len(blocks)-1):
            arrow = Arrow(blocks[i].get_right(), blocks[i+1].get_left(), buff=0.1)
            arrows.add(arrow)
            self.play(Create(arrow))
        
        self.wait(2)

        # Section 3: Mining
        self.clear_scene()
        title3 = Text("Mining & Proof-of-Work", font_size=36).to_edge(UP)
        self.play(Write(title3))

        block = VGroup(
            Rectangle(height=2, width=4, color=GOLD),
            Text("Block Data", font_size=24),
            Text("Nonce: 12345", font_size=20, color=YELLOW)
        ).arrange(DOWN, buff=0.2)
        self.play(Create(block))

        hash_text = Text("Hash: 0000a1b2c3...", font_size=24, color=RED).shift(DOWN*2)
        self.play(Write(hash_text))
        self.wait()

        mining_arrows = VGroup(*[
            Arrow(block.get_bottom(), hash_text.get_top(), color=BLUE)
            for _ in range(3)
        ])
        self.play(LaggedStart(
            *[GrowArrow(arrow) for arrow in mining_arrows],
            lag_ratio=0.3
        ))
        self.wait(2)

        # Section 4: Decentralization
        self.clear_scene()
        title4 = Text("Decentralized Network", font_size=36).to_edge(UP)
        self.play(Write(title4))

        nodes = VGroup(*[
            VGroup(
                Circle(radius=0.3, color=BLUE),
                Text(f"Node {i+1}", font_size=18)
            ).arrange(DOWN, buff=0.1) 
            for i in range(6)
        ]).arrange_in_grid(2, 3, buff=1)
        
        self.play(LaggedStart(*[FadeIn(node) for node in nodes], lag_ratio=0.2))
        
        connections = VGroup()
        for i, node in enumerate(nodes):
            for other in nodes[i+1:]:
                connections.add(Line(node.get_center(), other.get_center(), color=GREY, stroke_width=1))
        
        self.play(Create(connections), run_time=3)
        self.wait(2)

    def clear_scene(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
